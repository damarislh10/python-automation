
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_emisor ='correo_e'
email_contrasena = 'contraseña'

email_receptor = 'email_r'


asunto = 'Seremos grandes nueva foto'
cuerpo = """
Solo mirame y fijate que somos dos corazones redondos y lindos *-*
"""

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto

em.set_content(cuerpo)

# Adjuntar archivos

with open('BINGO2204.jpg', 'rb') as file:
    file_data = file.read()
    file_tipo =  imghdr.what(file.name)
    file_nombre = file.name
    em.add_attachment(file_data, filename = file_nombre, subtype=file_tipo, maintype= 'image')

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(email_emisor, email_contrasena)
    smtp.sendmail(email_emisor,email_receptor, em.as_string())