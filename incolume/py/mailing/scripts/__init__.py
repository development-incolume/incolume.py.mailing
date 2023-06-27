""""""
import smtplib
import email.message
import logging

__author__ = "@britodfbr"  # pragma: no cover


def send_gmail(
    smtp_user: str,
    smtp_pwd: str,
    smtp_server: str = None,
    smtp_port: int = 0,
    sender: str = '',
    reciver: str = '',
    content: str = '',
    content_type: str = 'plain',
    subject: str = '',
):
    """Baseado em https://pastebin.com/raw/JhsNiFqN"""
    smtp_server = smtp_server or 'smtp.gmail.com'
    smtp_port = smtp_port or 587
    smtp_pwd = smtp_pwd or '---'
    content = content or 'Mensagem de corpo do email'
    subject = subject or "Assunto do E-mail"
    sender = sender or 'remetente@gmail.com'
    reciver = reciver or 'destinatario@gmail.com'

    msg = email.message.Message()
    msg['Subject'] = subject

    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e
    # depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = sender
    msg['To'] = reciver
    msg.add_header('Content-Type', content_type)
    msg.set_payload(content)

    s = smtplib.SMTP(f'{smtp_server}: {smtp_port}')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(smtp_user, smtp_pwd)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    logging.debug('Email enviado')
    return True
