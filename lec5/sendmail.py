# -*- coding: cp1251 -*-
import smtplib
from email.MIMEText import MIMEText

# отправитель
me = 'me@bk.ru'
# получатель
you = 'you@gmail.com'
# текст письма
text = 'Это тестовое письмо!\nС наилучшими пожеланиями!'
text = unicode(text, "cp1251").encode("koi8-r")
# заголовок письма
subj = 'Привет от Python'

# параметры SMTP-сервера
server = "194.67.23.114" # "smtp.bk.ru"
port = 25
user_name = "userName"
user_passwd = "userPass"

# формирование сообщения
msg = MIMEText(text, "", "cp1251")
msg['Subject'] = subj
msg['From'] = me
msg['To'] = you

# отправка
s = smtplib.SMTP(server, port)
s.starttls()
s.login(user_name, user_passwd)
s.sendmail(me, you, msg.as_string())
s.quit()
