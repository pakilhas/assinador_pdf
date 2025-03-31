import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from PIL import Image
import io

# Configuração dos diretórios fixos
BASE_DIR = "H:\\Meu Drive\\dev\\assinador_pdf"
PDF_DIR = os.path.join(BASE_DIR, "pdf")
IMG_DIR = os.path.join(BASE_DIR, "img")
OUTPUT_DIR = os.path.join(BASE_DIR, "feito")

def add_image_to_pdf(input_pdf_path, output_pdf_path, image_path, position, size):
    """
    Adiciona uma imagem a todas as páginas de um PDF na posição especificada.
    """
    # Abrir o PDF original
    pdf_reader = PdfReader(input_pdf_path)
    pdf_writer = PdfWriter()
    
    # Carregar a imagem
    img = Image.open(image_path)
    img_reader = ImageReader(image_path)
    
    # Processar cada página
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        mediabox = page.mediabox
        
        # Criar um PDF temporário com a imagem
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Calcular posição
        page_width = float(mediabox.upper_right[0])
        page_height = float(mediabox.upper_right[1])
        
        img_width, img_height = float(size[0]), float(size[1])
        x = page_width - img_width - float(position[0])  # margem direita
        y = float(position[1])  # margem inferior
        
        # Desenhar a imagem
        can.drawImage(img_reader, x, y, 
                     width=img_width, 
                     height=img_height, 
                     mask='auto')
        can.save()
        
        # Mesclar com a página original
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])
        pdf_writer.add_page(page)
    
    # Salvar o PDF resultante
    with open(output_pdf_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)
    return output_pdf_path

def main():
    print("=== Sistema de Adição de Assinatura a PDF ===")
    
    # Solicitar apenas os nomes dos arquivos
    pdf_name = input("Digite o nome do arquivo PDF (ex: documento.pdf): ").strip()
    img_name = input("Digite o nome do arquivo de imagem (ex: assinatura.png): ").strip()
    
    # Construir os caminhos completos
    input_pdf = os.path.join(PDF_DIR, pdf_name)
    image_file = os.path.join(IMG_DIR, img_name)
    
    # Criar nome do arquivo de saída
    output_name = f"assinado_{pdf_name}"
    output_pdf = os.path.join(OUTPUT_DIR, output_name)
    
    # Verificar arquivos
    if not os.path.exists(input_pdf):
        print(f"Erro: O arquivo PDF '{input_pdf}' não foi encontrado.")
        return
    if not os.path.exists(image_file):
        print(f"Erro: A imagem '{image_file}' não foi encontrada.")
        return
    
    # Configurações
    position = (50, 50)  # (direita, inferior) em pontos
    size = (100, 50)     # (largura, altura) em pontos
    
    try:
        print("Processando...")
        output_path = add_image_to_pdf(input_pdf, output_pdf, image_file, position, size)
        print(f"Sucesso! PDF assinado salvo como: {output_name}")
        print(f"Caminho completo: {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()