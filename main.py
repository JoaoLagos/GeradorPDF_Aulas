"""
main.py - Arquivo da interface gráfica do Gerador de PDF.

Este arquivo contém a implementação da interface gráfica do Gerador de PDF,
usando a biblioteca Tkinter. Ele inclui funções para exibir instruções, processar
uma sequência de páginas, lidar com casos de sucesso e falha, e interagir com o
módulo create_pdf para gerar PDFs conforme especificado pelo usuário.

"""

import tkinter as tk
from tkinter import messagebox
import create_pdf
import sys

def exibir_instrucoes():
    """
    Exibe uma caixa de mensagem com instruções sobre o formato de entrada para o gerador de PDFs.
    """

    instrucoes = """
CRIADOR DE PDF'S DE AULAS
=======================================
    
"Crie facilmente arquivos PDF personalizados para suas aulas com este programa simples."
    
Digite as páginas desejadas no seguinte formato:
Exemplos:
    - '1,3,5' para gerar os PDFs da AULA 1, AULA 3 e AULA 5.
    - '1:4,6,9,21:24' para gerar os PDFs da AULA 1 a AULA 4, AULA 6, AULA 9, AULA 21 a AULA 24.
    - '1,5:9,12' para gerar os PDFs da AULA 1, AULA 5 a AULA 9, AULA 12.
    
=======================================
"""
    messagebox.showinfo("Instruções", instrucoes)

def processar():
    """
    Processa a sequência de páginas inserida pelo usuário, chamando a função de sucesso ou falha com base na validade da entrada.
    """

    sequencia = entrada.get()
    # Verifica se a entrada é válida
    if all(part.isdigit() or part == ':' or part == ',' or part == " " for part in sequencia):
        sucesso(sequencia)
    else:
        falha()

def sucesso(sequencia):
    """
    Realiza o processamento da sequência de páginas, criando os PDFs devidos e exibe uma mensagem de sucesso com os PDFs criados.
    """

    # PROCESSAMENTO
    # Remove os espaços
    sequencia = sequencia.replace(" ", "")

    # Gera os PDFS através da sequência 
    create_pdf.generate_pdfs(sequencia)


    # Mensagem de sucesso
    content = "PDFs criados com sucesso.\n\nPDFs criados:"
    for aula in create_pdf.lista:
        content += f"\n    - AULA {aula}"
    content += f"\n\n* Seus PDFs se encontram na Área de Trabalho."

    create_pdf.lista = []

    messagebox.showinfo("AVISO!", content)
    sys.exit()

def falha():
        """
    Exibe uma mensagem de falha em caso de entrada inválida.
    """
        
        content = """
Entrada inválida. Por favor, insira novamente.\n
Caso deseje saber o formato de entrada, vá em INSTRUÇÕES.
"""

        messagebox.showinfo("AVISO!", content)

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de PDF")

# Definir as dimensões da janela
janela.geometry("400x267")

# Estilizar a janela
janela.configure(bg="#263238")  # Cor de fundo
janela.resizable(False, False)  # Tornar a janela não redimensionável

# Adicionar colunas à janela
janela.grid_columnconfigure(0, weight=1)  # Coluna 0
janela.grid_columnconfigure(1, weight=1)  # Coluna 1 (coluna do meio)
janela.grid_columnconfigure(2, weight=1)  # Coluna 2

# Adicionar widgets à janela usando grid
label_titulo = tk.Label(janela, text="Gerador de PDF", font=("Arial", 16), bg="#263238", fg="#D7FFD6")
label_titulo.grid(row=0, column=1, pady=10)

# Adicionar um Frame simulando o efeito de sublinhado SUPERIOR
frame_linha = tk.Frame(janela, bg="#4CAF50", height=2)
frame_linha.grid(row=0, column=1, pady=(0, 30), sticky="we")
# Adicionar um Frame simulando o efeito de sublinhado INFERIOR
frame_linha = tk.Frame(janela, bg="#4CAF50", height=2)
frame_linha.grid(row=0, column=1, pady=(30,0), sticky="we")


label_mensagem = tk.Label(janela, text="Insira a sequência de páginas:", bg="#263238", fg="white")
label_mensagem.grid(row=2, column=1)

entrada = tk.Entry(janela, width=30, font=("Arial", 12))
entrada.grid(row=3, column=1, pady=10)

botao_processar = tk.Button(janela, text="PROCESSAR!", command=processar, bg="#4CAF50", fg="white", font=("Consolas", 12, "bold"), width=12, height=2)
botao_processar.grid(row=4, column=1, pady=10)

# Linha Divisória Horizontal
frame_linha = tk.Frame(janela, bg="#4CAF50", height=1)
frame_linha.grid(row=4, column=1, pady=(90,0), sticky="we")

# Botão de Instruções
botao_instrucoes = tk.Button(janela, text="INSTRUÇÕES", command=exibir_instrucoes, bg="#4CAF50", fg="white", font=("Consolas", 9, "bold"), width=12, height=1)
botao_instrucoes.grid(row=5, column=1, pady=20)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
