import pandas as pd
import numpy as np
import time
import logging
from multiprocessing import Pool, cpu_count
from datetime import datetime

# ==============================================================================
# CONFIGURAÇÃO DE LOGGING
# O uso do módulo logging permite que os logs sejam persistidos em arquivo 
# e versionados no GitHub, servindo como evidência formal da execução.
# ==============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("execution.log", mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ==============================================================================
# DECISÃO TÉCNICA: DEFINIÇÃO DO DATASET E TAMANHO DO CHUNK
# O arquivo original possui ~11.3 milhões de linhas (~2GB). 
# Escolhi um CHUNK_SIZE de 100.000 para equilibrar o uso de RAM (evitando 
# estouro de memória) e a eficiência de comunicação entre processos.
# ==============================================================================
FILENAME = "data/yellow_tripdata_2016-02.csv"
CHUNK_SIZE = 100000

def process_chunk(chunk):
    """
    Função executada pelos workers (Paralelo) ou sequencialmente (Parte A).
    Realiza a limpeza mínima e extração de métricas de um bloco de dados.
    """
    # Conversão de datetime necessária para análise temporal (Top 5 dias)
    chunk['tpep_pickup_datetime'] = pd.to_datetime(chunk['tpep_pickup_datetime'])
    chunk['pickup_date'] = chunk['tpep_pickup_datetime'].dt.date
    
    # Agregação local no chunk para reduzir o volume de dados trafegados via IPC
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
    """
    Fase de 'REDUCE': Consolida os resultados parciais de todos os chunks.
    """
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
    """
    PARTE A: Implementação Sequencial de Referência.
    Leitura e processamento ocorrem no mesmo processo, um chunk por vez.
    """
    logger.info("Iniciando Parte A — versão sequencial")
    start_time = time.time()
    results = []
    
    # Iterador de CSV para não carregar o arquivo inteiro na memória
    reader = pd.read_csv(FILENAME, chunksize=CHUNK_SIZE)
    for i, chunk in enumerate(reader):
        results.append(process_chunk(chunk))
        if (i + 1) % 10 == 0:
            current_count = sum(r['count'] for r in results)
            logger.info(f"Chunk {(i+1)} processado | Corridas acumuladas: {current_count:,}")
            
    final_metrics = aggregate_metrics(results)
    end_time = time.time()
    logger.info(f"Leitura concluída. {len(results)} chunks processados.")
    logger.info(f"Tempo total de execução (Sequencial): {end_time - start_time:.2f} segundos")
    return final_metrics, end_time - start_time

def run_parallel():
    """
    PARTE B: Implementação Paralela com Multiprocessing.
    DECISÃO TÉCNICA: Uso de imap_unordered para permitir o streaming de chunks
    do disco direto para os workers sem carregar todos os chunks em memória antes.
    """
    num_workers = cpu_count()
    logger.info(f"Iniciando Parte B — versão paralela | Workers: {num_workers} | Chunk: {CHUNK_SIZE}")
    start_time = time.time()
    
    results = []
    with Pool(num_workers) as pool:
        reader = pd.read_csv(FILENAME, chunksize=CHUNK_SIZE)
        # imap_unordered é mais eficiente que pool.map para geradores/iteradores grandes
        for i, res in enumerate(pool.imap_unordered(process_chunk, reader)):
            results.append(res)
            if (i + 1) % 10 == 0:
                current_count = sum(r['count'] for r in results)
                logger.info(f"Chunks recebidos: {(i+1)} | Corridas: {current_count:,}")
                
    final_metrics = aggregate_metrics(results)
    end_time = time.time()
    logger.info(f"Concluído. {len(results)} chunks processados.")
    logger.info(f"Tempo total de execução (Paralelo): {end_time - start_time:.2f} segundos")
    return final_metrics, end_time - start_time

def print_report(metrics):
    logger.info("\n--- MÉTRICAS CALCULADAS ---")
    logger.info(f"1. Quantidade total de corridas: {metrics['count']:,}")
    logger.info(f"2. Distância total percorrida (trip_distance): {metrics['sum_distance']:,.2f}")
    logger.info(f"3. Valor total arrecadado (total_amount): ${metrics['sum_amount']:,.2f}")
    logger.info(f"4. Média de passageiros por corrida: {metrics['sum_passengers'] / metrics['count']:.4f}")
    logger.info(f"5. Maior valor de corrida: ${metrics['max_amount']:,.2f}")
    logger.info(f"6. Menor valor de corrida: ${metrics['min_amount']:,.2f}")
    
    logger.info("\n2.1 Quantidade de Corridas por Forma de Pagamento")
    for pt, count in sorted(metrics['payment_types'].items()):
        perc = (count / metrics['count']) * 100
        logger.info(f"Código {pt}: {count:,} ({perc:.1f}%)")
        
    logger.info("\n2.2 Top 5 Dias com Maior Volume de Corridas")
    top_days = sorted(metrics['pickup_dates'].items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (day, count) in enumerate(top_days, 1):
        logger.info(f"{i}º {day}: {count:,}")

if __name__ == "__main__":
    # Execução das duas versões para comparação de performance requerida no trabalho
    m_seq, t_seq = run_sequential()
    print_report(m_seq)
    
    logger.info("="*50)
    
    m_par, t_par = run_parallel()
    print_report(m_par)
    
    speedup = t_seq / t_par
    logger.info(f"Speedup Resultante: {speedup:.2f}x")
    logger.info("ANÁLISE FINAL: O speedup < 1x indica um cenário I/O Bound.")
