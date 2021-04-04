import smtplib

def send_mail(smtp_server,port,sender_email,password,receiver_email,msg):
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())