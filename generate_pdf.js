const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    const browser = await puppeteer.launch({ headless: "new" });
    const page = await browser.newPage();
    
    const htmlContent = `
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; }
            h1 { text-align: center; font-size: 22px; margin-bottom: 5px; }
            h2 { font-size: 18px; border-bottom: 2px solid #2E75B6; padding-bottom: 5px; margin-top: 30px; color: #2E75B6; }
            h3 { font-size: 16px; margin-top: 20px; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
            th { background-color: #D5E8F0; }
            .header-table td { border: 1px solid #ccc; }
            .header-info { text-align: center; font-weight: bold; font-size: 18px; margin-bottom: 30px; }
            .footer { font-size: 10px; text-align: center; margin-top: 50px; border-top: 1px solid #ccc; padding-top: 10px; }
            pre { background: #f4f4f4; padding: 10px; border-left: 5px solid #2E75B6; font-size: 11px; overflow-x: auto; }
            .speedup { font-weight: bold; color: #d9534f; }
        </style>
    </head>
    <body>
        <h1>DIRETORIA DE EDUCAÇÃO CONTINUADA — IEC</h1>
        <div class="header-info">Processamento Distribuído com Divisão e Conquista</div>
        
        <table class="header-table">
            <tr><td><strong>Disciplina</strong></td><td>ARMAZENAMENTO E PROCESSAMENTO MASSIVO E DISTRIBUÍDO DE DADOS</td></tr>
            <tr><td><strong>Curso</strong></td><td>Engenharia de Dados</td></tr>
            <tr><td><strong>Professor</strong></td><td>Ricardo Brito Alves</td></tr>
            <tr><td><strong>Trabalho</strong></td><td>Processamento Distribuído - Parte B (Paralelismo)</td></tr>
            <tr><td><strong>Grupo</strong></td><td>Alfredo Neto, Carlos, Cláudio Pontes, Dgeison Serrão Peixoto, Eduardo Hosda, Francisco Duclou</td></tr>
            <tr><td><strong>Data</strong></td><td>28 de abril de 2026</td></tr>
            <tr><td><strong>GitHub</strong></td><td><a href="https://github.com/cllaud99/trabalho-paralelismo-parteb">https://github.com/cllaud99/trabalho-paralelismo-parteb</a></td></tr>
        </table>

        <h2>1. MÉTRICAS CALCULADAS</h2>
        <p>As métricas a seguir foram obtidas a partir do processamento completo do arquivo <strong>yellow_tripdata_2016-02.csv</strong> (11.382.049 registros). Os resultados foram produzidos pelas versões sequencial (Parte A) e paralela (Parte B), com valores idênticos em ambas.</p>
        
        <table>
            <thead>
                <tr><th>#</th><th>Métrica</th><th>Resultado</th></tr>
            </thead>
            <tbody>
                <tr><td>1</td><td>Quantidade total de corridas</td><td>11.382.049</td></tr>
                <tr><td>2</td><td>Distância total percorrida (trip_distance)</td><td>57.601.849,97</td></tr>
                <tr><td>3</td><td>Valor total arrecadado (total_amount)</td><td>$ 177.589.959,19</td></tr>
                <tr><td>4</td><td>Média de passageiros por corrida (passenger_count)</td><td>1,6552</td></tr>
                <tr><td>5</td><td>Maior valor de corrida (total_amount)</td><td>$ 154.832.14</td></tr>
                <tr><td>6</td><td>Menor valor de corrida (total_amount)</td><td>$ -450,30</td></tr>
            </tbody>
        </table>

        <h2>2. DETALHAMENTO POR FORMA DE PAGAMENTO E DATA</h2>
        <h3>2.1 Quantidade de Corridas por Forma de Pagamento (payment_type)</h3>
        <table>
            <thead>
                <tr><th>Código</th><th>Descrição</th><th>Quantidade de Corridas</th><th>Participação (%)</th></tr>
            </thead>
            <tbody>
                <tr><td>1</td><td>Cartão de crédito (Credit card)</td><td>7.680.359</td><td>67,5%</td></tr>
                <tr><td>2</td><td>Dinheiro (Cash)</td><td>3.647.035</td><td>32,0%</td></tr>
                <tr><td>3</td><td>Sem cobrança (No charge)</td><td>40.274</td><td>0,4%</td></tr>
                <tr><td>4</td><td>Disputa (Dispute)</td><td>14.381</td><td>0,1%</td></tr>
            </tbody>
        </table>

        <h3>2.2 Top 5 Dias com Maior Volume de Corridas</h3>
        <table>
            <thead>
                <tr><th>Posição</th><th>Data</th><th>Quantidade de Corridas</th></tr>
            </thead>
            <tbody>
                <tr><td>1º</td><td>13 de fevereiro de 2016</td><td>448.611</td></tr>
                <tr><td>2º</td><td>27 de fevereiro de 2016</td><td>440.935</td></tr>
                <tr><td>3º</td><td>26 de fevereiro de 2016</td><td>437.798</td></tr>
                <tr><td>4º</td><td>12 de fevereiro de 2016</td><td>434.350</td></tr>
                <tr><td>5º</td><td>11 de fevereiro de 2016</td><td>431.206</td></tr>
            </tbody>
        </table>

        <h2>3. COMPARAÇÃO DE DESEMPENHO — SEQUENCIAL VS. PARALELO</h2>
        <table>
            <thead>
                <tr><th>Versão</th><th>Implementação</th><th>Tempo de Execução</th><th>Speedup</th></tr>
            </thead>
            <tbody>
                <tr><td>Parte A</td><td>Sequencial (unithread)</td><td>11,18 s</td><td>1,00x (baseline)</td></tr>
                <tr><td>Parte B</td><td>Paralela (multiprocessing, 28 workers)</td><td>13,85 s</td><td class="speedup">0,81x</td></tr>
            </tbody>
        </table>

        <h2>4. ANÁLISE E DISCUSSÃO</h2>
        <h3>4.1 A versão paralela foi mais rápida?</h3>
        <p>Neste cenário específico, a versão paralela apresentou um desempenho ligeiramente inferior à sequencial (Speedup de 0.81x). Isso ocorre devido ao overhead de criação e gerenciamento de múltiplos processos (28 workers) superando o ganho computacional em um ambiente onde o gargalo principal é a leitura do disco (I/O Bound).</p>
        
        <h3>4.2 Gargalo de I/O</h3>
        <p>Como os dados estão em um único arquivo CSV de grande porte, a leitura sequencial pelo processo pai limita a velocidade com que os dados chegam aos workers. Em sistemas com armazenamento SSD convencional ou limitados por largura de banda de memória, o custo de serialização de dados para os processos filhos anula os benefícios do paralelismo.</p>

        <h2>5. LOGS DE EXECUÇÃO (RESUMO)</h2>
        <pre>
[00:34:45] Iniciando Parte A — versão sequencial
[00:34:56] Chunk 110 processado | Corridas acumuladas: 11,000,000 | Tempo: 10.8s
Tempo total de execução: 11.18 segundos

[00:34:57] Iniciando Parte B — versão paralela
Workers: 28 | Chunk: 100000
[00:35:10] Chunks recebidos: 110 | Corridas: 11,000,000 | Tempo: 13.5s
Tempo paralelo de execução: 13.85 segundos
        </pre>

        <h2>6. ESPECIFICAÇÕES TÉCNICAS</h2>
        <table>
            <tr><td><strong>Linguagem</strong></td><td>Python 3.12</td></tr>
            <tr><td><strong>Bibliotecas</strong></td><td>pandas, numpy, multiprocessing</td></tr>
            <tr><td><strong>Ambiente</strong></td><td>Linux (WSL2), 28 CPUs lógicas</td></tr>
            <tr><td><strong>Dataset</strong></td><td>yellow_tripdata_2016-02.csv (11.3M linhas, ~2GB)</td></tr>
        </table>

        <div class="footer">
            Relatório gerado em 28 de abril de 2026 — Disciplina: Armazenamento e Processamento Massivo e Distribuído de Dados — PUC / IEC
        </div>
    </body>
    </html>
    `;

    await page.setContent(htmlContent);
    await page.pdf({
        path: 'Relatorio_Trabalho_Paralelismo_ParteB.pdf',
        format: 'A4',
        printBackground: true,
        margin: { top: '20px', right: '20px', bottom: '20px', left: '20px' }
    });

    await browser.close();
    console.log('PDF gerado com sucesso: Relatorio_Trabalho_Paralelismo_ParteB.pdf');
})();
