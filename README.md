# ✨  Gerador de capas em arquivo PDF para Aulas

<p align="left">
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge"/>
    <!-- <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge"/> -->
    <img src="https://img.shields.io/github/license/JoaoLagos/GeradorPDF_Aulas?color=blue&style=for-the-badge"/>
</p>

Um programa simples em Python (sem interface gráfica) para criar facilmente capas personalizadas em arquivo PDF para suas aulas.
<br><hr>
<p align="center"><b>Propósito:</b></p>
<br>Ao estudar, eu salvo (e separo) meu conteúdo estudado por aula, e ao final salvo em  um PDF essas aulas. <br><br>
Entretanto, esse procedimento torna-se oneroso quando lidamos com múltiplas aulas. Por exemplo, se tivermos quatro aulas (digamos Aula 3, Aula 4, Aula 5 e Aula 6), seria necessária a criação de quatro PDFs distintos, com o conteúdo interno "Aula X" (onde X é o número correspondente à aula). Esse processo demandaria tempo considerável, pois envolveria a escrita do conteúdo "Aula X" dentro de um arquivo .docx (por exemplo), e a transformação para PDF, repetindo esse processo para cada aula. A complexidade aumenta significativamente quando extrapolamos esse cenário para um maior número de aulas, como dez, por exemplo 😵.<br><br>
Diante dessa realidade, desenvolvi um programa que automatiza esse processo para o usuário. Ao inserir as aulas desejadas, respeitando o formato de entrada, o aplicativo gera os PDFs "Aula X" correspondentes em menos de 5 segundos. Essa solução visa otimizar o tempo e esforço dedicados à criação manual dos documentos, proporcionando uma experiência mais eficiente e ágil no gerenciamento do conteúdo estudado.
<hr>

<br>
<div style="display: inline_block; text-align: center;">
    <img src="./assets/photo1.png" alt="Photo 1">
    <hr>
    <img src="./assets/photo2.png" alt="Photo 2">
    <img src="./assets/photo3.png" alt="Photo 3">
</div>


##  :hammer_and_wrench: Instruções de Uso

1. **Execute o Programa:**
   - Certifique-se de ter o Python instalado em seu sistema.
   - Clone este repositório para o seu computador.

     ```bash
     git clone https://github.com/JoaoLagos/GeradorPDF_Aulas.git
     ```

   - Navegue até o diretório do projeto.

     ```bash
     cd GeradorPDF_Aulas
     ```

   - Execute o programa.

     ```bash
     python create_pdf.py
     ```

2. **Digite as Páginas Desejadas:**
   - O programa solicitará que você insira as páginas desejadas no formato especificado.

     ```
     Digite as páginas desejadas no seguinte formato:
     Exemplos:
     - '1,3,5' para gerar os PDFs da AULA 1, AULA 3 e AULA 5.
     - '1:4,6,9,21:24' para gerar os PDFs da AULA 1 a AULA 4, AULA 6, AULA 9, AULA 21 a AULA 24.
     - '1,5:9,12' para gerar os PDFs da AULA 1, AULA 5 a AULA 9, AULA 12.
     ```

3. **PDFs Gerados:**
   - Os PDFs serão gerados na sua Área de Trabalho (Desktop).

## :white_check_mark: Requisitos

- Python 3.x

## :handshake: Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## :memo: Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
