from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm

def add_footer(canvas, doc):
    canvas.saveState()
    # Usar uma fonte um pouco menor e garantir que o texto não transborde
    canvas.setFont('Helvetica', 8)
    footer_text = f"Relatório gerado em 28 de abril de 2026 — Disciplina: Armazenamento e Processamento Massivo e Distribuído de Dados — PUC / IEC — Página {doc.page}"
    # Centralizar com limite de margem
    canvas.drawCentredString(A4[0] / 2.0, 1.0 * cm, footer_text)
    canvas.restoreState()

def create_pdf():
    # Margens seguras
    doc = SimpleDocTemplate("Relatorio_Trabalho_Paralelismo_ParteB_Final.pdf", pagesize=A4,
                            rightMargin=2.0*cm, leftMargin=2.0*cm,
                            topMargin=2.0*cm, bottomMargin=2.5*cm)
    
    styles = getSampleStyleSheet()
    
    # Estilos customizados
    styles.add(ParagraphStyle(name='Center', alignment=1, fontSize=16, spaceAfter=12, fontName="Helvetica-Bold", leading=20))
    styles.add(ParagraphStyle(name='Heading1_Custom', fontSize=14, spaceBefore=15, spaceAfter=12, fontName="Helvetica-Bold", textColor=colors.HexColor("#2E75B6"), leading=18))
    styles.add(ParagraphStyle(name='Heading2_Custom', fontSize=12, spaceBefore=12, spaceAfter=8, fontName="Helvetica-Bold", textColor=colors.HexColor("#2E75B6"), leading=14))
    
    # Estilo para células de tabela (permite quebra de linha)
    cell_style = ParagraphStyle(name='TableCell', fontSize=10, fontName="Helvetica", leading=12)
    cell_style_bold = ParagraphStyle(name='TableCellBold', fontSize=10, fontName="Helvetica-Bold", leading=12)
    
    styles.add(ParagraphStyle(name='Normal_Custom', fontSize=11, spaceAfter=10, fontName="Helvetica", leading=14, alignment=4)) # JUSTIFY
    styles.add(ParagraphStyle(name='Code_Custom', fontSize=8, fontName="Courier", spaceAfter=10, leftIndent=0.3*cm, rightIndent=0.3*cm, textColor=colors.HexColor("#333333"), leading=10, backColor=colors.HexColor("#F4F4F4"), borderPadding=5))
    styles.add(ParagraphStyle(name='Small_Oblique', fontSize=9, fontName="Helvetica-Oblique", leading=11))

    elements = []

    # Cabeçalho
    elements.append(Paragraph("DIRETORIA DE EDUCAÇÃO CONTINUADA — IEC", styles['Center']))
    elements.append(Paragraph("Processamento Distribuído com Divisão e Conquista", styles['Center']))
    elements.append(Spacer(1, 0.5*cm))

    # Tabela de Identificação (Todos os campos com Paragraph para evitar transbordo)
    data_header = [
        [Paragraph("<b>Disciplina</b>", cell_style), Paragraph("ARMAZENAMENTO E PROCESSAMENTO MASSIVO E DISTRIBUÍDO DE DADOS", cell_style)],
        [Paragraph("<b>Curso</b>", cell_style), Paragraph("Engenharia de Dados", cell_style)],
        [Paragraph("<b>Professor</b>", cell_style), Paragraph("Ricardo Brito Alves", cell_style)],
        [Paragraph("<b>Trabalho</b>", cell_style), Paragraph("Processamento Distribuído - Parte B (Paralelismo)", cell_style)],
        [Paragraph("<b>Grupo</b>", cell_style), Paragraph("Alfredo Neto, Carlos, Cláudio Pontes, Dgeison Serrão Peixoto, Eduardo Hosda, Francisco Duclou", cell_style)],
        [Paragraph("<b>Data</b>", cell_style), Paragraph("28 de abril de 2026", cell_style)],
        [Paragraph("<b>GitHub</b>", cell_style), Paragraph("<u>https://github.com/cllaud99/trabalho-paralelismo-parteb</u>", cell_style)]
    ]
    
    # Largura útil = 21cm - 4cm = 17cm
    t_header = Table(data_header, colWidths=[3.5*cm, 13.5*cm])
    t_header.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#D5E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t_header)
    elements.append(Spacer(1, 0.8*cm))

    # Seção 1
    elements.append(Paragraph("1. MÉTRICAS CALCULADAS", styles['Heading1_Custom']))
    elements.append(Paragraph("As métricas a seguir foram obtidas a partir do processamento completo do arquivo <i>yellow_tripdata_2016-02.csv</i> (11.382.049 registros).", styles['Normal_Custom']))

    data_metrics = [
        [Paragraph("<b>#</b>", cell_style), Paragraph("<b>Métrica</b>", cell_style), Paragraph("<b>Resultado</b>", cell_style)],
        ["1", Paragraph("Quantidade total de corridas", cell_style), Paragraph("11.382.049", cell_style)],
        ["2", Paragraph("Distância total percorrida (trip_distance)", cell_style), Paragraph("57.601.849,97", cell_style)],
        ["3", Paragraph("Valor total arrecadado (total_amount)", cell_style), Paragraph("$ 177.589.959,19", cell_style)],
        ["4", Paragraph("Média de passageiros por corrida (passenger_count)", cell_style), Paragraph("1,6552", cell_style)],
        ["5", Paragraph("Maior valor de corrida (total_amount)", cell_style), Paragraph("$ 154.832,14", cell_style)],
        ["6", Paragraph("Menor valor de corrida (total_amount)", cell_style), Paragraph("$ -450,30", cell_style)]
    ]
    t_metrics = Table(data_metrics, colWidths=[1*cm, 11*cm, 5*cm])
    t_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (2,1), (2,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    elements.append(t_metrics)
    elements.append(Paragraph("Obs.: o valor mínimo negativo (-$ 450,30) é um dado real do dataset, correspondente a estornos e disputas registrados pela NYC TLC.", styles['Small_Oblique']))

    # Seção 2
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("2. DETALHAMENTO POR FORMA DE PAGAMENTO E DATA", styles['Heading1_Custom']))
    elements.append(Paragraph("2.1 Quantidade de Corridas por Forma de Pagamento", styles['Heading2_Custom']))

    data_payment = [
        [Paragraph("<b>Código</b>", cell_style), Paragraph("<b>Descrição</b>", cell_style), Paragraph("<b>Quantidade</b>", cell_style), Paragraph("<b>Part. (%)</b>", cell_style)],
        ["1", Paragraph("Cartão de crédito (Credit card)", cell_style), Paragraph("7.680.359", cell_style), "67,5%"],
        ["2", Paragraph("Dinheiro (Cash)", cell_style), Paragraph("3.647.035", cell_style), "32,0%"],
        ["3", Paragraph("Sem cobrança (No charge)", cell_style), Paragraph("40.274", cell_style), "0,4%"],
        ["4", Paragraph("Disputa (Dispute)", cell_style), Paragraph("14.381", cell_style), "0,1%"]
    ]
    t_payment = Table(data_payment, colWidths=[2*cm, 8*cm, 4*cm, 3*cm])
    t_payment.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (2,1), (3,-1), 'RIGHT'),
    ]))
    elements.append(t_payment)

    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("2.2 Top 5 Dias com Maior Volume de Corridas", styles['Heading2_Custom']))
    data_days = [
        [Paragraph("<b>Posição</b>", cell_style), Paragraph("<b>Data</b>", cell_style), Paragraph("<b>Quantidade</b>", cell_style)],
        ["1º", "13 de fevereiro de 2016", "448.611"],
        ["2º", "27 de fevereiro de 2016", "440.935"],
        ["3º", "26 de fevereiro de 2016", "437.798"],
        ["4º", "12 de fevereiro de 2016", "434.350"],
        ["5º", "11 de fevereiro de 2016", "431.206"]
    ]
    t_days = Table(data_days, colWidths=[3*cm, 9*cm, 5*cm])
    t_days.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (2,1), (2,-1), 'RIGHT'),
    ]))
    elements.append(t_days)

    elements.append(PageBreak())

    # Seção 3
    elements.append(Paragraph("3. COMPARAÇÃO DE DESEMPENHO — SEQUENCIAL VS. PARALELO", styles['Heading1_Custom']))
    data_perf = [
        [Paragraph("<b>Versão</b>", cell_style), Paragraph("<b>Implementação</b>", cell_style), Paragraph("<b>Tempo</b>", cell_style), Paragraph("<b>Speedup</b>", cell_style)],
        ["Parte A", Paragraph("Sequencial (unithread)", cell_style), "11,18 s", "1,00x"],
        ["Parte B", Paragraph("Paralela (multiprocessing, 28 workers)", cell_style), "13,85 s", Paragraph("<font color='red'>0,81x</font>", cell_style)]
    ]
    t_perf = Table(data_perf, colWidths=[3*cm, 8*cm, 3.5*cm, 2.5*cm])
    t_perf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#D5E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(t_perf)

    # Seção 4
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("4. ANÁLISE E DISCUSSÃO", styles['Heading1_Custom']))
    elements.append(Paragraph("4.1 A versão paralela foi mais rápida?", styles['Heading2_Custom']))
    elements.append(Paragraph("O ganho de desempenho observado foi negativo (0,81x). Isso demonstra que o overhead de criação e coordenação de 28 processos superou o ganho computacional em uma tarefa limitada por I/O.", styles['Normal_Custom']))
    
    # Seção 5
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("5. LOGS DE EXECUÇÃO", styles['Heading1_Custom']))
    log_text = "[00:34:45] Iniciando Parte A — versão sequencial<br/>[00:34:56] Leitura concluída. 114 chunks processados.<br/>Tempo total: 11.18s<br/><br/>[00:34:57] Iniciando Parte B — versão paralela (28 workers)<br/>[00:35:10] Concluído. 114 chunks processados.<br/>Tempo paralelo: 13.85s"
    elements.append(Paragraph(log_text, styles['Code_Custom']))

    # Seção 6
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("6. ESPECIFICAÇÕES TÉCNICAS", styles['Heading1_Custom']))
    data_tech = [
        [Paragraph("<b>Linguagem</b>", cell_style), "Python 3.12"],
        [Paragraph("<b>Bibliotecas</b>", cell_style), "pandas, numpy, multiprocessing"],
        [Paragraph("<b>Ambiente</b>", cell_style), "Linux (WSL2), 28 CPUs lógicas"],
        [Paragraph("<b>Dataset</b>", cell_style), "yellow_tripdata_2016-02.csv (~2GB)"]
    ]
    t_tech = Table(data_tech, colWidths=[4*cm, 13*cm])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#D5E8F0")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elements.append(t_tech)

    doc.build(elements, onFirstPage=add_footer, onLaterPages=add_footer)
    print("PDF corrigido gerado com sucesso!")

if __name__ == "__main__":
    create_pdf()
