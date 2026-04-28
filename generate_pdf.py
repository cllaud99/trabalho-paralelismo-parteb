from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.drawCentredString(A4[0] / 2.0, 1.5 * cm, f"Relatório gerado em 28 de abril de 2026 — Disciplina: Armazenamento e Processamento Massivo e Distribuído de Dados — PUC / IEC — Página {doc.page}")
    canvas.restoreState()

def create_pdf():
    # Aumentar margens para evitar cortes e garantir legibilidade
    doc = SimpleDocTemplate("Relatorio_Trabalho_Paralelismo_ParteB_Final.pdf", pagesize=A4,
                            rightMargin=2.5*cm, leftMargin=2.5*cm,
                            topMargin=2.5*cm, bottomMargin=2.5*cm)
    
    styles = getSampleStyleSheet()
    
    # Estilos customizados
    styles.add(ParagraphStyle(name='Center', alignment=1, fontSize=16, spaceAfter=12, fontName="Helvetica-Bold", leading=20))
    styles.add(ParagraphStyle(name='Heading1_Custom', fontSize=14, spaceBefore=15, spaceAfter=12, fontName="Helvetica-Bold", textColor=colors.HexColor("#2E75B6"), leading=18))
    styles.add(ParagraphStyle(name='Heading2_Custom', fontSize=12, spaceBefore=12, spaceAfter=8, fontName="Helvetica-Bold", textColor=colors.HexColor("#2E75B6"), leading=14))
    styles.add(ParagraphStyle(name='Normal_Custom', fontSize=11, spaceAfter=10, fontName="Helvetica", leading=14, alignment=4)) # alignment 4 is JUSTIFY
    styles.add(ParagraphStyle(name='Code_Custom', fontSize=9, fontName="Courier", spaceAfter=10, leftIndent=0.5*cm, rightIndent=0.5*cm, textColor=colors.HexColor("#333333"), leading=12, backColor=colors.HexColor("#F4F4F4"), borderPadding=5))
    styles.add(ParagraphStyle(name='Small_Oblique', fontSize=9, fontName="Helvetica-Oblique", leading=11))

    elements = []

    # Cabeçalho do documento
    elements.append(Paragraph("DIRETORIA DE EDUCAÇÃO CONTINUADA — IEC", styles['Center']))
    elements.append(Paragraph("Processamento Distribuído com Divisão e Conquista", styles['Center']))
    elements.append(Spacer(1, 0.5*cm))

    # Tabela de Identificação
    data_header = [
        [Paragraph("<b>Disciplina</b>", styles['Normal']), "ARMAZENAMENTO E PROCESSAMENTO MASSIVO E DISTRIBUÍDO DE DADOS"],
        [Paragraph("<b>Curso</b>", styles['Normal']), "Engenharia de Dados"],
        [Paragraph("<b>Professor</b>", styles['Normal']), "Ricardo Brito Alves"],
        [Paragraph("<b>Trabalho</b>", styles['Normal']), "Processamento Distribuído - Parte B (Paralelismo)"],
        [Paragraph("<b>Grupo</b>", styles['Normal']), "Alfredo Neto, Carlos, Cláudio Pontes, Dgeison Serrão Peixoto, Eduardo Hosda, Francisco Duclou"],
        [Paragraph("<b>Data</b>", styles['Normal']), "28 de abril de 2026"],
        [Paragraph("<b>GitHub</b>", styles['Normal']), "https://github.com/cllaud99/trabalho-paralelismo-parteb"]
    ]
    
    # Ajustar larguras das colunas para caber na página (A4 largura = 21cm, menos 5cm de margens = 16cm)
    t_header = Table(data_header, colWidths=[3.5*cm, 12.5*cm])
    t_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#D5E8F0")),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(t_header)
    elements.append(Spacer(1, 1*cm))

    # Seção 1: Métricas
    elements.append(Paragraph("1. MÉTRICAS CALCULADAS", styles['Heading1_Custom']))
    elements.append(Paragraph("As métricas a seguir foram obtidas a partir do processamento completo do arquivo <i>yellow_tripdata_2016-02.csv</i> (11.382.049 registros). Os resultados foram produzidos pelas versões sequencial (Parte A) e paralela (Parte B), com valores idênticos em ambas, confirmando a corretude da implementação paralela.", styles['Normal_Custom']))

    data_metrics = [
        ["#", "Métrica", "Resultado"],
        ["1", "Quantidade total de corridas", "11.382.049"],
        ["2", "Distância total percorrida (trip_distance)", "57.601.849,97"],
        ["3", "Valor total arrecadado (total_amount)", "$ 177.589.959,19"],
        ["4", "Média de passageiros por corrida (passenger_count)", "1,6552"],
        ["5", "Maior valor de corrida (total_amount)", "$ 154.832,14"],
        ["6", "Menor valor de corrida (total_amount)", "$ -450,30"]
    ]
    t_metrics = Table(data_metrics, colWidths=[1*cm, 10.5*cm, 4.5*cm])
    t_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (0,1), (0,-1), 'CENTER'),
        ('ALIGN', (2,1), (2,-1), 'RIGHT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(t_metrics)
    elements.append(Spacer(1, 0.2*cm))
    elements.append(Paragraph("Obs.: o valor mínimo negativo (-$ 450,30) é um dado real do dataset, correspondente a estornos e disputas registrados pela NYC TLC.", styles['Small_Oblique']))

    # Seção 2: Detalhamento
    elements.append(Spacer(1, 0.8*cm))
    elements.append(Paragraph("2. DETALHAMENTO POR FORMA DE PAGAMENTO E DATA", styles['Heading1_Custom']))
    elements.append(Paragraph("2.1 Quantidade de Corridas por Forma de Pagamento (payment_type)", styles['Heading2_Custom']))

    data_payment = [
        ["Código", "Descrição", "Quantidade", "Part. (%)"],
        ["1", "Cartão de crédito (Credit card)", "7.680.359", "67,5%"],
        ["2", "Dinheiro (Cash)", "3.647.035", "32,0%"],
        ["3", "Sem cobrança (No charge)", "40.274", "0,4%"],
        ["4", "Disputa (Dispute)", "14.381", "0,1%"]
    ]
    t_payment = Table(data_payment, colWidths=[2*cm, 7.5*cm, 4*cm, 2.5*cm])
    t_payment.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (0,1), (0,-1), 'CENTER'),
        ('ALIGN', (2,1), (3,-1), 'RIGHT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(t_payment)

    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("2.2 Top 5 Dias com Maior Volume de Corridas (tpep_pickup_datetime)", styles['Heading2_Custom']))
    data_days = [
        ["Posição", "Data", "Quantidade"],
        ["1º", "13 de fevereiro de 2016", "448.611"],
        ["2º", "27 de fevereiro de 2016", "440.935"],
        ["3º", "26 de fevereiro de 2016", "437.798"],
        ["4º", "12 de fevereiro de 2016", "434.350"],
        ["5º", "11 de fevereiro de 2016", "431.206"]
    ]
    t_days = Table(data_days, colWidths=[3*cm, 8.5*cm, 4.5*cm])
    t_days.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (0,1), (0,-1), 'CENTER'),
        ('ALIGN', (2,1), (2,-1), 'RIGHT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(t_days)

    elements.append(PageBreak())

    # Seção 3: Desempenho
    elements.append(Paragraph("3. COMPARAÇÃO DE DESEMPENHO — SEQUENCIAL VS. PARALELO", styles['Heading1_Custom']))
    data_perf = [
        ["Versão", "Implementação", "Tempo", "Speedup"],
        ["Parte A", "Sequencial (unithread)", "11,18 s", "1,00x (baseline)"],
        ["Parte B", "Paralela (multiprocessing, 28 workers)", "13,85 s", "0,81x"]
    ]
    t_perf = Table(data_perf, colWidths=[2.5*cm, 7.5*cm, 3.5*cm, 2.5*cm])
    t_perf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('TEXTCOLOR', (3,2), (3,2), colors.red), # Destaque speedup < 1
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (2,1), (3,-1), 'RIGHT'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(t_perf)

    # Seção 4: Análise
    elements.append(Spacer(1, 0.8*cm))
    elements.append(Paragraph("4. ANÁLISE E DISCUSSÃO", styles['Heading1_Custom']))
    elements.append(Paragraph("4.1 A versão paralela foi mais rápida?", styles['Heading2_Custom']))
    elements.append(Paragraph("O ganho de desempenho observado foi negativo (0,81x). A versão paralela executou em 13,85 segundos contra 11,18 segundos da versão sequencial. Na prática, o overhead de gerenciamento de processos e comunicação entre eles superou a capacidade de processamento paralelo disponível para este volume de dados.", styles['Normal_Custom']))
    
    elements.append(Paragraph("4.2 Por que o speedup foi baixo?", styles['Heading2_Custom']))
    elements.append(Paragraph("O gargalo identificado foi de entrada e saída (I/O), não de processamento de CPU. A leitura do arquivo CSV ocorre sequencialmente pelo processo principal. Como o tempo de processamento por linha é relativamente baixo comparado ao tempo de leitura do disco, os workers passam grande parte do tempo aguardando novos chunks de dados.", styles['Normal_Custom']))
    
    elements.append(Paragraph("4.3 O tamanho do chunk influenciou?", styles['Heading2_Custom']))
    elements.append(Paragraph("Foi utilizado um chunk de 100.000 linhas. Variações neste tamanho poderiam reduzir o overhead de comunicação, mas não resolveriam o gargalo principal de I/O de leitura sequencial do arquivo físico.", styles['Normal_Custom']))

    # Seção 5: Logs
    elements.append(Spacer(1, 0.8*cm))
    elements.append(Paragraph("5. LOGS DE EXECUÇÃO", styles['Heading1_Custom']))
    elements.append(Paragraph("5.1 Parte A — Versão Sequencial", styles['Heading2_Custom']))
    log_seq = """[00:34:45] Iniciando Parte A — versão sequencial<br/>
[00:34:46] Chunk 10 processado | Corridas acumuladas: 1,000,000 | Tempo: 1.0s<br/>
[00:34:56] Chunk 110 processado | Corridas acumuladas: 11,000,000 | Tempo: 10.8s<br/>
Leitura concluída. 114 chunks processados.<br/>
Tempo total de execução: 11.18 segundos"""
    elements.append(Paragraph(log_seq, styles['Code_Custom']))

    elements.append(Paragraph("5.2 Parte B — Versão Paralela", styles['Heading2_Custom']))
    log_par = """[00:34:57] Iniciando Parte B — versão paralela<br/>
Workers: 28 | Chunk: 100000<br/>
[00:35:01] Chunks recebidos: 10 | Corridas: 1,000,000 | Tempo: 4.0s<br/>
[00:35:10] Chunks recebidos: 110 | Corridas: 11,000,000 | Tempo: 13.5s<br/>
Concluído. 114 chunks processados.<br/>
Tempo paralelo de execução: 13.85 segundos"""
    elements.append(Paragraph(log_par, styles['Code_Custom']))

    # Seção 6: Técnica
    elements.append(Spacer(1, 0.8*cm))
    elements.append(Paragraph("6. ESPECIFICAÇÕES TÉCNICAS", styles['Heading1_Custom']))
    data_tech = [
        [Paragraph("<b>Linguagem</b>", styles['Normal']), "Python 3.12"],
        [Paragraph("<b>Bibliotecas</b>", styles['Normal']), "pandas 3.0.2, numpy 2.4.4, multiprocessing"],
        [Paragraph("<b>Paralelismo</b>", styles['Normal']), "multiprocessing.Pool com imap_unordered"],
        [Paragraph("<b>Ambiente</b>", styles['Normal']), "Linux (WSL2), 28 CPUs lógicas"],
        [Paragraph("<b>Dataset</b>", styles['Normal']), "yellow_tripdata_2016-02.csv (11.3M registros, ~2GB)"]
    ]
    t_tech = Table(data_tech, colWidths=[4*cm, 12*cm])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#D5E8F0")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(t_tech)

    doc.build(elements, onFirstPage=add_footer, onLaterPages=add_footer)
    print("PDF ajustado com sucesso: Relatorio_Trabalho_Paralelismo_ParteB_Final.pdf")

if __name__ == "__main__":
    create_pdf()
