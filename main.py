import pandas as pd
import numpy as np
import time
from multiprocessing import Pool, cpu_count
from datetime import datetime

FILENAME = "data/yellow_tripdata_2016-02.csv"
CHUNK_SIZE = 100000

def process_chunk(chunk):
    # Convert datetime
    chunk['tpep_pickup_datetime'] = pd.to_datetime(chunk['tpep_pickup_datetime'])
    chunk['pickup_date'] = chunk['tpep_pickup_datetime'].dt.date
    
    metrics = {
        'count': len(chunk),
        'sum_distance': chunk['trip_distance'].sum(),
        'sum_amount': chunk['total_amount'].sum(),
        'sum_passengers': chunk['passenger_count'].sum(),
        'max_amount': chunk['total_amount'].max(),
        'min_amount': chunk['total_amount'].min(),
        'payment_types': chunk['payment_type'].value_counts().to_dict(),
        'pickup_dates': chunk['pickup_date'].value_counts().to_dict()
    }
    return metrics

def aggregate_metrics(results):
    total_metrics = {
        'count': 0,
        'sum_distance': 0.0,
        'sum_amount': 0.0,
        'sum_passengers': 0,
        'max_amount': -float('inf'),
        'min_amount': float('inf'),
        'payment_types': {},
        'pickup_dates': {}
    }
    
    for res in results:
        total_metrics['count'] += res['count']
        total_metrics['sum_distance'] += res['sum_distance']
        total_metrics['sum_amount'] += res['sum_amount']
        total_metrics['sum_passengers'] += res['sum_passengers']
        total_metrics['max_amount'] = max(total_metrics['max_amount'], res['max_amount'])
        total_metrics['min_amount'] = min(total_metrics['min_amount'], res['min_amount'])
        
        for pt, count in res['payment_types'].items():
            total_metrics['payment_types'][pt] = total_metrics['payment_types'].get(pt, 0) + count
            
        for d, count in res['pickup_dates'].items():
            total_metrics['pickup_dates'][d] = total_metrics['pickup_dates'].get(d, 0) + count
            
    return total_metrics

def run_sequential():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando Parte A — versão sequencial")
    start_time = time.time()
    results = []
    
    reader = pd.read_csv(FILENAME, chunksize=CHUNK_SIZE)
    for i, chunk in enumerate(reader):
        results.append(process_chunk(chunk))
        if (i + 1) % 10 == 0:
            current_count = sum(r['count'] for r in results)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Chunk {(i+1)} processado | Corridas acumuladas: {current_count:,} | Tempo: {time.time() - start_time:.1f}s")
            
    final_metrics = aggregate_metrics(results)
    end_time = time.time()
    print(f"Leitura concluída. {len(results)} chunks processados.")
    print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")
    return final_metrics, end_time - start_time

def run_parallel():
    num_workers = cpu_count()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando Parte B — versão paralela")
    print(f"Workers: {num_workers} | Chunk: {CHUNK_SIZE}")
    start_time = time.time()
    
    results = []
    with Pool(num_workers) as pool:
        reader = pd.read_csv(FILENAME, chunksize=CHUNK_SIZE)
        # Using imap_unordered for better performance with streaming
        for i, res in enumerate(pool.imap_unordered(process_chunk, reader)):
            results.append(res)
            if (i + 1) % 10 == 0:
                current_count = sum(r['count'] for r in results)
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Chunks recebidos: {(i+1)} | Corridas: {current_count:,} | Tempo: {time.time() - start_time:.1f}s")
                
    final_metrics = aggregate_metrics(results)
    end_time = time.time()
    print(f"Concluído. {len(results)} chunks processados.")
    print(f"Tempo paralelo de execução: {end_time - start_time:.2f} segundos")
    return final_metrics, end_time - start_time

def print_report(metrics):
    print("\n--- MÉTRICAS CALCULADAS ---")
    print(f"1. Quantidade total de corridas: {metrics['count']:,}")
    print(f"2. Distância total percorrida (trip_distance): {metrics['sum_distance']:,.2f}")
    print(f"3. Valor total arrecadado (total_amount): ${metrics['sum_amount']:,.2f}")
    print(f"4. Média de passageiros por corrida: {metrics['sum_passengers'] / metrics['count']:.4f}")
    print(f"5. Maior valor de corrida: ${metrics['max_amount']:,.2f}")
    print(f"6. Menor valor de corrida: ${metrics['min_amount']:,.2f}")
    
    print("\n2.1 Quantidade de Corridas por Forma de Pagamento")
    for pt, count in sorted(metrics['payment_types'].items()):
        perc = (count / metrics['count']) * 100
        print(f"Código {pt}: {count:,} ({perc:.1f}%)")
        
    print("\n2.2 Top 5 Dias com Maior Volume de Corridas")
    top_days = sorted(metrics['pickup_dates'].items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (day, count) in enumerate(top_days, 1):
        print(f"{i}º {day}: {count:,}")

if __name__ == "__main__":
    m_seq, t_seq = run_sequential()
    print_report(m_seq)
    
    print("\n" + "="*50 + "\n")
    
    m_par, t_par = run_parallel()
    print_report(m_par)
    
    speedup = t_seq / t_par
    print(f"\nSpeedup: {speedup:.2f}x")
