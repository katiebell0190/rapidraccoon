import smtplib
from email import encoders
from email.mime.base import MIMEBase
from typing import Text
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def send_email():
    subject = input("Enter subject: ")
    body = input("Enter message: ")
    senders_email = 'katieb0190@outlook.com'
    receivers_email = ['katieb0190@outlook.com.','caitlin.waszgis@physiciansmutual.com','amaggioni@aiminstitute.org']
    password = getpass.getpass(prompt='Enter password: ')

    message = MIMEMultipart()
    message['From'] = senders_email
    message['To'] = ",".join(receivers_email)
    message['Subject'] = subject

    message.attach(MIMEText(body,'plain'))
    filename = r'C:\Users\Owner\Desktop\Callers to Coders\Project\inforce.csv'
    with open(filename,'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename={filename}'
        )
    message.attach(part)
    text = message.as_string()
    with smtplib.SMTP("smtp.office365.com:587") as server:
        server.starttls()
        server.login(senders_email,password)
        server.sendmail(senders_email,receivers_email,text)
    print('Email sent')