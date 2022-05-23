import baixarDados
import enviarEmail
import gerarGrafico
import caminhosArquivos
import time
import os

with open('email.txt') as f:
    email = f.read()

gerarGrafico.gerarPDF()

answer = input("O e-mail que você deseja enviar é: "+email+"? [S/N]:   ")
if answer.lower() in ["s","S", "sim","Sim","SIM"]:
     to_email = email
     print("\nPREPARANDO E-MAIL PARA ENVIO\n")
elif answer.lower() in ["N", "n","NAO", "NÃO", "Não", "Nao", "nao", "não"]:
     to_email = input("Digite o e-mail desejado: " )
else:
     print("ERRO")

enviarEmail.enviarPrecos(to_email)


data = time.strftime("%d-%m-%Y")
os.remove(caminhosArquivos.caminhoDiretorio()+'panorama_'+data+'.pdf')
os.remove(caminhosArquivos.caminhoDiretorio()+'panorama_'+data+'.png')