import caminhosArquivos as path
import smtplib
import os
import time
# from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações
from_email = 'YOUREMAIL@gmail.com'
senha = 'YOURPASSWORD'
data = time.strftime("%d-%m-%Y")
ano = time.strftime("%Y")
mes = time.strftime("%m")

def enviarPrecos(to_email):
    msg = MIMEMultipart()
    msg['Subject'] = 'Envio Diário Preços: '+data
    msg['From'] = from_email
    msg['To'] = to_email

    caminhoGrafico = path.caminhoDiretorio() + 'panorama_' + data + '.pdf'
    caminhoDessem = path.caminhoDiretorio() + path.nomeArquivoDessem()
    caminhoPreco = path.caminhoDiretorio() + path.nomeArquivoPreco()
    message = 'Arquivos do dia '+data
    msg.attach(MIMEText(message, "plain"))

    try:
        with open(caminhoGrafico, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment', filename="panorama_"+data+'.pdf')
        msg.attach(attach)

        with open(caminhoPreco, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="csv")
        attach.add_header('Content-Disposition', 'attachment', filename="preco_horario_"+data+'.csv')
        msg.attach(attach)

    except Exception as e:
        print("\nARQUIVO PARA ENVIO DE E-MAIL NÃO ENCONTRADO\n" + str(e))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, senha)
            smtp.send_message(msg)
            print("\nE-MAIL ENVIADO COM SUCESSO\n")
    except Exception as e:
        print("\nERRO NO ENVIO DO E-MAIL\n" + str(e))


