import pandas as pd
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from PIL import Image, ImageDraw, ImageFont
import os
import locale 
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Dicionário contendo informações dos templates
templates = {
    '1': {
        'moldura': 'templates/moldura1.png',
        'fonte_titulo': 'fonts/andalucia.ttf',
        'fonte_nome': 'fonts/PlayfairDisplay-Regular.ttf',
        'fonte_conteudo': 'fonts/Arial.ttf',
        'assinatura': 'assinaturas/assinatura_responsavel.png'
    },
    '2': {
        'moldura': 'templates/moldura2.png',
        'fonte_titulo': 'fonts/lucida-fax-regular.ttf',
        'fonte_nome': 'fonts/raleway.ttf',
        'fonte_conteudo': 'fonts/PTSerif-Web-Regular.ttf',
        'assinatura': 'assinaturas/assinatura_responsavel.png'
    }
}

# Função para gerar o certificado
def gerar_certificado(nome, curso, carga_horaria, local, data, data_inicio, data_fim, instituicao, template_escolhido):
   
    # Tamanho da página A4 em modo paisagem
    largura, altura = landscape(A4)
    
    # Definir o nome do arquivo PDF
    arquivo_pdf = f"certificados/{nome}.pdf"
    
    # Cria o canvas para o PDF
    c = canvas.Canvas(arquivo_pdf, pagesize=landscape(A4))
    
    # Carregar a moldura do template como imagem
    moldura = template_escolhido['moldura']
    c.drawImage(moldura, 0, 0, width=largura, height=altura)

    # Definir as posições dos textos e fontes
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(largura / 2, altura - 30, instituicao)
    
    c.setFont("Helvetica", 18)
    c.drawCentredString(largura / 2, altura - 210, "Certificamos para todos os fins que")

    c.setFont("Helvetica", 26)
    c.drawCentredString(largura / 2, altura - 273, f"{nome}")
    
    c.setFont("Helvetica", 16)
    c.drawCentredString(largura / 2, altura - 310, f"concluiu o curso {curso}, realizado na cidade de {local},")
    c.drawCentredString(largura / 2, altura - 340, f"no período de {data_inicio} a {data_fim}, com carga horária de {carga_horaria} horas.")
    
    c.setFont("Helvetica", 12)
    c.drawCentredString(largura / 2, altura - 390, f"{local}, {data}.")

    # Inserindo assinatura digital
    assinatura = template_escolhido['assinatura']
    c.drawImage(assinatura, largura / 2 - 100, altura - 500, width=200, height=100)

    c.setFont("Helvetica", 10)
    c.drawCentredString(largura / 2, altura - 520, "Assinatura do responsável")

    # Salvar o PDF e finalizar o canvas
    c.save()
    print(f"Certificado gerado para {nome}")

# Leitura do arquivo Excel
df = pd.read_excel('certificados_dados.xlsx')

# Solicitar escolha de template
template_escolhido = input("Escolha o template (1, 2): ")
template = templates[template_escolhido]

# Criar diretório para salvar os certificados, se não existir
if not os.path.exists('certificados'):
    os.makedirs('certificados')

# Gerar certificados para cada linha do Excel
for index, row in df.iterrows():
    nome_participante = row['Nome']
    curso = row['Curso']
    carga_horaria = row['Carga Horária']
    local = row['Local']
    data_inicio = row['Data de Início'].strftime('%d/%m/%Y')
    data_fim = row['Data Final'].strftime('%d/%m/%Y')
    data = row['Data'].strftime('%d de %B de %Y')  # Formatar a data ('%d de %B de %Y') ('%d/%m/%Y')
    instituicao = row['Instituição'] 
    
    gerar_certificado(nome_participante, curso, carga_horaria, local, data, data_inicio, data_fim, instituicao, template)
