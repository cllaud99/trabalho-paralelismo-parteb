const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType, PageBreak } = require('docx');
const fs = require('fs');

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const headerShading = { fill: "D5E8F0", type: ShadingType.CLEAR };

const doc = new Document({
    styles: {
        default: { document: { run: { font: "Arial", size: 24 } } },
        paragraphStyles: [
            { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
              run: { size: 32, bold: true, font: "Arial", color: "2E75B6" },
              paragraph: { spacing: { before: 400, after: 240 }, outlineLevel: 0 } },
            { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
              run: { size: 28, bold: true, font: "Arial", color: "2E75B6" },
              paragraph: { spacing: { before: 300, after: 180 }, outlineLevel: 1 } },
        ]
    },
    sections: [{
        children: [
            new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text: "DIRETORIA DE EDUCAÇÃO CONTINUADA — IEC", bold: true, size: 28 })]
            }),
            new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text: "Processamento Distribuído com Divisão e Conquista", bold: true, size: 28 })]
            }),
            new Paragraph({ text: "\n" }),
            new Table({
                width: { size: 9360, type: WidthType.DXA },
                columnWidths: [3000, 6360],
                rows: [
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Disciplina", bold: true })] })] }),
                        new TableCell({ borders, children: [new Paragraph("ARMAZENAMENTO E PROCESSAMENTO MASSIVO E DISTRIBUÍDO DE DADOS")] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Curso", bold: true })] })] }),
                        new TableCell({ borders, children: [new Paragraph("Engenharia de Dados")] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Professor", bold: true })] })] }),
                        new TableCell({ borders, children: [new Paragraph("Ricardo Brito Alves")] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Trabalho", bold: true })] })] }),
                        new TableCell({ borders, children: [new Paragraph("Processamento Distribuído - Parte B (Paralelismo)")] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Grupo", bold: true })] })] }),
                        new TableCell({ borders, children: [new Paragraph("Alfredo Neto, Carlos, Cláudio Pontes, Dgeison Serrão Peixoto, Eduardo Hosda, Francisco Duclou")] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Data", bold: true })] })] }),
                        new TableCell({ borders, children: [new Paragraph("28 de abril de 2026")] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "GitHub", bold: true })] })] }),
                        new TableCell({ borders, children: [new Paragraph("https://github.com/cllaud99/trabalho-paralelismo-parteb")] })
                    ] })
                ]
            }),

            new Paragraph({ text: "1. MÉTRICAS CALCULADAS", heading: HeadingLevel.HEADING_1 }),
            new Paragraph("As métricas a seguir foram obtidas a partir do processamento completo do arquivo yellow_tripdata_2016-02.csv (11.382.049 registros). Os resultados foram produzidos pelas versões sequencial (Parte A) e paralela (Parte B), com valores idênticos em ambas, confirmando a corretude da implementação paralela."),
            
            new Table({
                width: { size: 9360, type: WidthType.DXA },
                columnWidths: [800, 5560, 3000],
                rows: [
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "#", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Métrica", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Resultado", bold: true })] })] })
                    ] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("1")] }), new TableCell({ borders, children: [new Paragraph("Quantidade total de corridas")] }), new TableCell({ borders, children: [new Paragraph("11.382.049")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("2")] }), new TableCell({ borders, children: [new Paragraph("Distância total percorrida (trip_distance)")] }), new TableCell({ borders, children: [new Paragraph("57.601.849,97")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("3")] }), new TableCell({ borders, children: [new Paragraph("Valor total arrecadado (total_amount)")] }), new TableCell({ borders, children: [new Paragraph("$ 177.589.959,19")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("4")] }), new TableCell({ borders, children: [new Paragraph("Média de passageiros por corrida (passenger_count)")] }), new TableCell({ borders, children: [new Paragraph("1,6552")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("5")] }), new TableCell({ borders, children: [new Paragraph("Maior valor de corrida (total_amount)")] }), new TableCell({ borders, children: [new Paragraph("$ 154.832,14")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("6")] }), new TableCell({ borders, children: [new Paragraph("Menor valor de corrida (total_amount)")] }), new TableCell({ borders, children: [new Paragraph("$ -450,30")] })] })
                ]
            }),
            new Paragraph({ text: "Obs.: o valor mínimo negativo (-$ 450,30) é um dado real do dataset, correspondente a estornos e disputas registrados pela NYC TLC.", size: 18 }),

            new Paragraph({ text: "2. DETALHAMENTO POR FORMA DE PAGAMENTO E DATA", heading: HeadingLevel.HEADING_1 }),
            new Paragraph({ text: "2.1 Quantidade de Corridas por Forma de Pagamento (payment_type)", heading: HeadingLevel.HEADING_2 }),
            new Table({
                width: { size: 9360, type: WidthType.DXA },
                columnWidths: [1500, 4000, 2000, 1860],
                rows: [
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Código", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Descrição", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Quantidade", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Part. (%)", bold: true })] })] })
                    ] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("1")] }), new TableCell({ borders, children: [new Paragraph("Cartão de crédito (Credit card)")] }), new TableCell({ borders, children: [new Paragraph("7.680.359")] }), new TableCell({ borders, children: [new Paragraph("67,5%")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("2")] }), new TableCell({ borders, children: [new Paragraph("Dinheiro (Cash)")] }), new TableCell({ borders, children: [new Paragraph("3.647.035")] }), new TableCell({ borders, children: [new Paragraph("32,0%")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("3")] }), new TableCell({ borders, children: [new Paragraph("Sem cobrança (No charge)")] }), new TableCell({ borders, children: [new Paragraph("40.274")] }), new TableCell({ borders, children: [new Paragraph("0,4%")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("4")] }), new TableCell({ borders, children: [new Paragraph("Disputa (Dispute)")] }), new TableCell({ borders, children: [new Paragraph("14.381")] }), new TableCell({ borders, children: [new Paragraph("0,1%")] })] })
                ]
            }),

            new Paragraph({ text: "2.2 Top 5 Dias com Maior Volume de Corridas (tpep_pickup_datetime)", heading: HeadingLevel.HEADING_2 }),
            new Table({
                width: { size: 9360, type: WidthType.DXA },
                columnWidths: [2000, 4000, 3360],
                rows: [
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Posição", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Data", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Quantidade", bold: true })] })] })
                    ] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("1º")] }), new TableCell({ borders, children: [new Paragraph("13 de fevereiro de 2016")] }), new TableCell({ borders, children: [new Paragraph("448.611")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("2º")] }), new TableCell({ borders, children: [new Paragraph("27 de fevereiro de 2016")] }), new TableCell({ borders, children: [new Paragraph("440.935")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("3º")] }), new TableCell({ borders, children: [new Paragraph("26 de fevereiro de 2016")] }), new TableCell({ borders, children: [new Paragraph("437.798")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("4º")] }), new TableCell({ borders, children: [new Paragraph("12 de fevereiro de 2016")] }), new TableCell({ borders, children: [new Paragraph("434.350")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("5º")] }), new TableCell({ borders, children: [new Paragraph("11 de fevereiro de 2016")] }), new TableCell({ borders, children: [new Paragraph("431.206")] })] })
                ]
            }),

            new Paragraph({ children: [new PageBreak()] }),

            new Paragraph({ text: "3. COMPARAÇÃO DE DESEMPENHO — SEQUENCIAL VS. PARALELO", heading: HeadingLevel.HEADING_1 }),
            new Table({
                width: { size: 9360, type: WidthType.DXA },
                columnWidths: [2000, 4000, 2000, 1360],
                rows: [
                    new TableRow({ children: [
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Versão", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Implementação", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Tempo", bold: true })] })] }),
                        new TableCell({ borders, shading: headerShading, children: [new Paragraph({ children: [new TextRun({ text: "Speedup", bold: true })] })] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, children: [new Paragraph("Parte A")] }),
                        new TableCell({ borders, children: [new Paragraph("Sequencial (unithread)")] }),
                        new TableCell({ borders, children: [new Paragraph("11,18 s")] }),
                        new TableCell({ borders, children: [new Paragraph("1,00x (baseline)")] })
                    ] }),
                    new TableRow({ children: [
                        new TableCell({ borders, children: [new Paragraph("Parte B")] }),
                        new TableCell({ borders, children: [new Paragraph("Paralela (multiprocessing, 28 workers)")] }),
                        new TableCell({ borders, children: [new Paragraph("13,85 s")] }),
                        new TableCell({ borders, children: [new Paragraph("0,81x")] })
                    ] })
                ]
            }),

            new Paragraph({ text: "4. ANÁLISE E DISCUSSÃO", heading: HeadingLevel.HEADING_1 }),
            new Paragraph({ text: "4.1 A versão paralela foi mais rápida?", heading: HeadingLevel.HEADING_2 }),
            new Paragraph("O ganho de desempenho observado foi negativo (0,81x). A versão paralela executou em 13,85 segundos contra 11,18 segundos da versão sequencial. Na prática, o overhead de gerenciamento de processos e comunicação entre eles superou a capacidade de processamento paralelo disponível para este volume de dados."),
            
            new Paragraph({ text: "4.2 Por que o speedup foi baixo?", heading: HeadingLevel.HEADING_2 }),
            new Paragraph("O gargalo identificado foi de entrada e saída (I/O), não de processamento de CPU. A leitura do arquivo CSV ocorre sequencialmente pelo processo principal. Como o tempo de processamento por linha é relativamente baixo comparado ao tempo de leitura do disco, os workers passam grande parte do tempo aguardando novos chunks de dados."),
            
            new Paragraph({ text: "4.3 O tamanho do chunk influenciou?", heading: HeadingLevel.HEADING_2 }),
            new Paragraph("Foi utilizado um chunk de 100.000 linhas. Variações neste tamanho poderiam reduzir o overhead de comunicação, mas não resolveriam o gargalo principal de I/O de leitura sequencial do arquivo físico."),

            new Paragraph({ text: "5. LOGS DE EXECUÇÃO", heading: HeadingLevel.HEADING_1 }),
            new Paragraph({ text: "5.1 Parte A — Versão Sequencial", heading: HeadingLevel.HEADING_2 }),
            new Paragraph({ text: "[00:34:45] Iniciando Parte A — versão sequencial\n[00:34:46] Chunk 10 processado | Corridas acumuladas: 1,000,000 | Tempo: 1.0s\n[00:34:56] Chunk 110 processado | Corridas acumuladas: 11,000,000 | Tempo: 10.8s\nLeitura concluída. 114 chunks processados.\nTempo total de execução: 11.18 segundos", font: "Courier New", size: 18 }),

            new Paragraph({ text: "5.2 Parte B — Versão Paralela", heading: HeadingLevel.HEADING_2 }),
            new Paragraph({ text: "[00:34:57] Iniciando Parte B — versão paralela\nWorkers: 28 | Chunk: 100000\n[00:35:01] Chunks recebidos: 10 | Corridas: 1,000,000 | Tempo: 4.0s\n[00:35:10] Chunks recebidos: 110 | Corridas: 11,000,000 | Tempo: 13.5s\nConcluído. 114 chunks processados.\nTempo paralelo de execução: 13.85 segundos", font: "Courier New", size: 18 }),

            new Paragraph({ text: "6. ESPECIFICAÇÕES TÉCNICAS", heading: HeadingLevel.HEADING_1 }),
            new Table({
                width: { size: 9360, type: WidthType.DXA },
                columnWidths: [3000, 6360],
                rows: [
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("Linguagem")] }), new TableCell({ borders, children: [new Paragraph("Python 3.12")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("Bibliotecas")] }), new TableCell({ borders, children: [new Paragraph("pandas 3.0.2, numpy 2.4.4")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("Paralelismo")] }), new TableCell({ borders, children: [new Paragraph("multiprocessing.Pool com imap_unordered")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("Ambiente")] }), new TableCell({ borders, children: [new Paragraph("Linux (WSL2), 28 CPUs lógicas")] })] }),
                    new TableRow({ children: [new TableCell({ borders, children: [new Paragraph("Dataset")] }), new TableCell({ borders, children: [new Paragraph("yellow_tripdata_2016-02.csv (11.3M registros)")] })] })
                ]
            }),

            new Paragraph({ text: "\n\nRelatório gerado em 28 de abril de 2026 — Disciplina: Armazenamento e Processamento Massivo e Distribuído de Dados — PUC / IEC", alignment: AlignmentType.CENTER, size: 16 })
        ]
    }]
});

Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync("Relatorio_Trabalho_Paralelismo_ParteB_Final.docx", buffer);
    console.log("Documento final gerado com sucesso: Relatorio_Trabalho_Paralelismo_ParteB_Final.docx");
});
