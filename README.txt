### PyMailer
---
## Required
* [Python >= 3.8][link1]
## Send mail 
```python
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyMails import *

smtp_server = '' 
port = ''
sender_email = ''
password = ''
receiver_email = ''

## Html form
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Test mail'
msg['From'] = sender_email
msg['To'] = receiver_email

html = open('./html/mail.html','r+').read()
msg.attach(MIMEText(html, 'html'))

## Without html form
msg = MIMEText('Test')
msg['Subject'] = 'Test mail'
msg['From'] = sender_email
msg['To'] = receiver_email

send_mail(smtp_server,port,sender_email,password,receiver_email,msg);
```