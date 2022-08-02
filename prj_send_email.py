import smtplib
from email import encoders
from email.mime.base import MIMEBase
from typing import Text
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

#works
#SEND EMAIL WITH ATTACHMENT
def sendemail():
    subject = input("Enter subject: ")
    body = input("Enter message: ")
    senders_email = 'katieb0190@outlook.com'
    receivers_email = 'katieb0190@outlook.com'
    password = getpass.getpass(prompt='Enter password: ')

    #CREATE MULTIPART MESSAGE AND SET HEADERS
    message = MIMEMultipart()
    message['From'] = senders_email
    message['To'] = receivers_email
    message['Subject'] = subject

    #ADD BODY TO MAIL
    message.attach(MIMEText(body,'plain'))
    filename = r"C:\Users\Owner\Desktop\Callers to Coders\sample_attachment.txt"

    #Import FILE
    with open(filename,'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    #THIS ENCODES FILE CHARACTERS IN ASCII
    encoders.encode_base64(part)


    #THIS PART ADDS HEADER TO ATTACHMENT
    part.add_header(
        'Content-Disposition',
        f'attachment; filename={filename}'
        )

    #ADDS ATTACHMENT TO MESSAGE AND CONVERTS MESSAGE TO STRING
    message.attach(part)
    text = message.as_string()

    #LOG INTO SERVER USING SECURE CONNECTION 
    with smtplib.SMTP("smtp.office365.com:587") as server:
        server.starttls()
        server.login(senders_email,password)
        server.sendmail(senders_email,receivers_email,text)

    print('Email sent')
sendemail()