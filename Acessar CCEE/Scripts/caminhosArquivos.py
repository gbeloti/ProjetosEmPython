import time
import os

with open('diretorioDownload.txt') as f:
    dirDownload = f.read()

# Definir diretorio de entrada e saida de dados
def caminhoDiretorio():
    return dirDownload
# No geral o caminho é C:\\users\\(nome do usuario)\\Downloads\\

# Caminho para o Chrome Driver
def caminhoChromeDriver():
    return "C:\\ChromeDriver\\chromedriver.exe"

# Nome do arquivo preco diario
def nomeArquivoPreco():
    return "preco_horario.csv"

# Nome do arquivo DESSEM
def nomeArquivoDessem():
    nome = "DES_"
    ano = time.strftime("%Y")
    mes = time.strftime("%m")
    formato = ".zip"
    return nome+ano+mes+formato
