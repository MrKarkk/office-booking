from email.message import EmailMessage
import smtplib

def send_email(address, subject, text):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'adbuaziz@gmail.com'
    sender_password = 'kenx ouet hvrg znki'

    message = EmailMessage()
    message['From'] = sender_email
    message['To'] = address
    message['Subject'] = subject
    message.set_content(text)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)