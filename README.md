# Trabalho de Processamento Distribuído - Parte B (Paralelismo)

Este projeto implementa uma solução para o processamento massivo de dados do dataset **NYC Yellow Taxi Trip Data**, comparando uma abordagem sequencial (Parte A) com uma abordagem paralela utilizando a biblioteca `multiprocessing` (Parte B).

## 🚀 Objetivo
O objetivo principal é aplicar o paradigma de **Divisão e Conquista** para processar ~11.3 milhões de registros (~2GB) de forma eficiente, extraindo métricas como:
- Quantidade total de corridas.
- Distância total percorrida.
- Valor total arrecadado.
- Média de passageiros por corrida.
- Detalhamento por forma de pagamento.
- Top 5 dias com maior volume de corridas.

## 📁 Estrutura do Projeto
A organização dos arquivos segue o padrão exigido pelo exercício:
- `data/`: Diretório destinado ao dataset `yellow_tripdata_2016-02.csv`.
- `src/`: Contém o código-fonte principal (`solution.py`).
- `logs/`: Contém os logs detalhados da execução (`execution.log`).
- `Relatorio_Trabalho_Paralelismo_ParteB_Final.pdf`: Relatório formal com os resultados e evidências.

## 🛠️ Tecnologias Utilizadas
- **Python 3.12**
- **Pandas**: Manipulação de dados e leitura em blocos (`chunksize`).
- **Multiprocessing**: Implementação do paralelismo com `Pool` e `imap_unordered`.
- **UV**: Gerenciador de pacotes e ambiente virtual.

## 📈 Resultados Obtidos
A versão paralela utilizou **20 workers**, alcançando os seguintes tempos em ambiente de teste:
- **Tempo Sequencial**: ~14.30 segundos.
- **Tempo Paralelo**: ~10.73 segundos.
- **Speedup**: 1.33x

*Nota: O ganho de desempenho é limitado pela natureza I/O Bound da tarefa (leitura de disco de arquivos grandes).*

## 📖 Como Executar
1. Certifique-se de ter o [UV](https://github.com/astral-sh/uv) instalado.
2. Coloque o dataset em `data/yellow_tripdata_2016-02.csv`.
3. Execute o comando:
   ```bash
   uv run python src/solution.py
   ```
4. Os resultados serão exibidos no console e salvos em `logs/execution.log`.
