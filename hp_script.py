import pandas as pd
import smtplib
import datetime
from email.message import EmailMessage

csv = pd.read_csv("happy_birthday.csv")
today = datetime.datetime.now().strftime("%d/%m")
yearnow = datetime.datetime.now().strftime("%Y")


def send_email(to, message, subject):
    # Preparando o Email
    email = EmailMessage()
    email['from'] = 'Lucas Felipe'
    email['to'] = to
    email['subject'] = subject
    email.set_content(message)

    # Enviando Email
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("9cf3dd4a1csc396", "c16c8dsd61940d8")
        smtp.send_message(email)
        print(f"Email enviado para {to} com sucesso.")


for index, item in csv.iterrows():
    bday = datetime.datetime.strptime(item['data'], '%d/%m/%Y').strftime("%d/%m")

    if bday == today and yearnow != item['last_gz']:
        send_email(item['email'], item['msg'], f'Feliz Aniversário {item["nome"]}')
    else:
        print("Sem aniversários hoje")





