import smtplib
import ssl
import mimetypes
from email.message import EmailMessage


# 1- dados do Email
password = open('senha', 'r').read() #senha configurada do seu email
from_email = 'emailficticio123@gmail.com'
to_email = 'emaildodestinatario123@gmail.com'
subject = 'Automação'
body = '''
    Bom dia!!
    Qualquer duvida estou a disposição!
'''

# 2 - Montando a estrutura do email
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 3 - Adicionar anexo 
anexo = '' #anexo do email 

mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype = mime_type,  
        subtype = mime_subtype,
        filename = anexo 
    )
    
# 4 - Envio do Email 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )