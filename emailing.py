import smtplib
from email.message import EmailMessage
from string import Template #helps in substitue with texts
from pathlib import Path #similar to os

html=Template(Path('index_email.html').read_text())

email=EmailMessage()
email['from']='Sayam Bothra'
email['to']='bothrasayam007@gmail.com'
email['subject']="Learning to send automated emails"
email.set_content(html.substitue(name='Baby')) # this is still in html
email.set_content(html.substitue(name='Baby'),'html') # will parse the html code without having tags.
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # encryption-connecting securely to the server
    smtp.login('codingmaang@gmail.com','Maang@1511')
    smtp.send_message(email)
    print('all good boss!!')
