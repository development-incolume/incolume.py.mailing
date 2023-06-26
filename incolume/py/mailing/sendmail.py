"""Module sendmail"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import getenv
import logging

__author__ = "@britodfbr"  # pragma: no cover

load_dotenv()
host, port, user, pwd, sender, reciver, subject = (
    getenv('SMTP_HOST'),
    int(getenv('SMTP_PORT')),
    getenv('SMTP_USER'),
    getenv('SMTP_PWD'),
    getenv('SENDER'),
    getenv('RECIVER'),
    getenv('SUBJECT'),
)
logging.debug('%s %s %s %s %s', host, port, user, sender, reciver, subject)


with smtplib.SMTP(host=host, port=port) as server:
    server.ehlo()
    server.starttls()
    server.login(user, pwd)

    email_msg = MIMEMultipart()
    email_msg['To'] = reciver
    email_msg['From'] = sender
    email_msg['Subject'] = subject
    content = 'conteúdo do email'
    email_msg.attach(MIMEText(content, 'plain'))

    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
