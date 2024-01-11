"""
CRIADOR DE PDF'S DE AULAS
=====================================================================

Este programa permite criar facilmente arquivos PDF personalizados para suas aulas.

Instruções:
1. Execute o programa e siga as orientações abaixo.
2. Digite as páginas desejadas no formato especificado.
3. Exemplos:
    - '1,3,5' para gerar os PDFs da AULA 1, AULA 3 e AULA 5.
    - '1:4,6,9,21:24' para gerar os PDFs da AULA 1 a AULA 4, AULA 6, AULA 9, AULA 21 a AULA 24.
    - '1,5:9,12' para gerar os PDFs da AULA 1, AULA 5 a AULA 9, AULA 12.
    - 'q' para sair do programa.

=====================================================================
    
FUNÇÕES:
1. \033[1mget_input_pages()\033[0m
   - Descrição: Solicita ao usuário as páginas desejadas para a criação dos PDFs.
   - Entrada: Nenhuma.
   - Saída: Retorna a string das páginas desejadas inseridas pelo usuário.

2. \033[1mcreate_pdf(page_number)\033[0m
   - Descrição: Cria um arquivo PDF para uma página específica.
   - Entrada: Número da página desejada.
   - Saída: Um arquivo PDF com o conteúdo "AULA {page_number}" centralizado.

3. \033[1mgenerate_pdfs(input_pages)\033[0m
   - Descrição: Gera os PDFs conforme as páginas especificadas.
   - Entrada: String contendo as páginas desejadas no formato especificado.
   - Saída: Criação dos arquivos PDFs correspondentes.

=====================================================================
    
EXEMPLO DE USO:
if __name__ == "__main__":
    # Recebe as páginas desejadas como uma string
    input_pages = get_input_pages()

    # Chama a função para gerar os PDFs
    generate_pdfs(input_pages)

    print("PDFs criados com sucesso.")
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from colorama import init, Fore, Style

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

def get_input_pages():
    """
    Solicita ao usuário as páginas desejadas para a criação dos PDFs.

    Instruções:
    1. Digite as páginas desejadas no formato especificado.
    2. Exemplos:
        - '1,3,5' para gerar os PDFs da AULA 1, AULA 3 e AULA 5.
        - '1:4,6,9,21:24' para gerar os PDFs da AULA 1 a AULA 4, AULA 6, AULA 9, AULA 21 a AULA 24.
        - '1,5:9,12' para gerar os PDFs da AULA 1, AULA 5 a AULA 9, AULA 12.
        - 'q' para sair do programa.

    :return: String contendo as páginas desejadas inseridas pelo usuário.
    """

    while True:
        os.system('')  # Ativa as sequências de escape ANSI no Console Virtual

        print("\033[1;34mCRIADOR DE PDF'S DE AULAS\033[0m")
        print("=======================================================")
        print("\n\033[1m\"Crie facilmente arquivos PDF personalizados para suas aulas com este programa simples.\"\033[0m\n")
        print("\033[1;32mDigite as páginas desejadas no seguinte formato:\033[0m")
        print("\033[1;32mExemplos:\033[0m")
        print(f"    \033[1;32m- '1,3,5' para gerar os PDFs da \033[1;31mAULA 1\033[0m, \033[1;31mAULA 3\033[0m e \033[1;31mAULA 5\033[0m.\033[0m")
        print(f"    \033[1;32m- '1:4,6,9,21:24' para gerar os PDFs da \033[1;31mAULA 1\033[0m a \033[1;31mAULA 4\033[0m, \033[1;31mAULA 6\033[0m, \033[1;31mAULA 9\033[0m, \033[1;31mAULA 21\033[0m a \033[1;31mAULA 24\033[0m.\033[0m")
        print(f"    \033[1;32m- '1,5:9,12' para gerar os PDFs da \033[1;31mAULA 1\033[0m, \033[1;31mAULA 5\033[0m a \033[1;31mAULA 9\033[0m, \033[1;31mAULA 12\033[0m.\033[0m")
        print("\n=======================================================")

        input_pages = input("\nDigite sua escolha: ")
        
        # Verifica se a entrada é válida
        if all(part.isdigit() or part == ':' or part == ',' or part == " " for part in input_pages):
            input_pages = input_pages.replace(" ", "")
            print(input_pages)
            return input_pages
        else:
            print("\nEntrada inválida. Por favor, insira novamente.\n")

def create_pdf(page_number):
    """
    Cria um arquivo PDF para uma página específica e salva na Área de Trabalho.

    :param page_number: Número da página desejada.
    """
    
    # Configuração do arquivo PDF
    #pdf_file = f"{page_number}.pdf"
    pdf_file = os.path.join(desktop_path, f"{page_number}.pdf")
    c = canvas.Canvas(pdf_file, pagesize=A4)

    # Obtém as dimensões da página
    width, height = A4

    # Configuração do texto
    text = f"AULA {page_number}"
    font_size = 72

    # Calcula as coordenadas para centralizar verticalmente
    text_width, text_height = c.stringWidth(text, "Helvetica", font_size), font_size
    x = (width - text_width) / 2
    y = (height - text_height) / 2 + (72/2)

    # Desenha o texto na posição calculada
    c.setFont("Helvetica", font_size)
    c.drawString(x, y, text)

    # Salva o arquivo PDF
    c.save()

def generate_pdfs(input_pages):
    """
    Gera os PDFs conforme as páginas especificadas.

    Parâmetros:
    - input_pages (str): String contendo as páginas desejadas no formato especificado.

    Formato da Especificação:
    - O parâmetro 'input_pages' deve ser uma string contendo números inteiros separados por vírgula.
    - Para intervalos de páginas, utilize ':' para indicar o início e o fim do intervalo.
        Exemplos válidos:
            - '1,3,5' para gerar os PDFs da AULA 1, AULA 3 e AULA 5.
            - '1:4,6,9,21:24' para gerar os PDFs da AULA 1 a AULA 4, AULA 6, AULA 9, AULA 21 a AULA 24.
            - '1,5:9,12' para gerar os PDFs da AULA 1, AULA 5 a AULA 9, AULA 12.
    """

    # Divide as páginas com base nas vírgulas
    page_ranges = input_pages.split(',')

    # Loop sobre as páginas desejadas
    for page_range in page_ranges:
        # Divide o intervalo de páginas se houver um ':' presente
        start, _, end = page_range.partition(':')

        if end:  # Se houver um final especificado
            for page_number in range(int(start), int(end) + 1):
                create_pdf(page_number)
        else:
            # Caso contrário, só uma página é especificada
            page_number = int(start)
            create_pdf(page_number)

if __name__ == "__main__":
    # Recebe as páginas desejadas como uma string
    input_pages = get_input_pages()

    # Chama a função para gerar os PDFs
    generate_pdfs(input_pages)

    print("PDFs criados com sucesso.")
