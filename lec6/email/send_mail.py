import sys, smtplib, socket
from getpass import getpass

server = "smtp.yandex.ru"
fromaddr = "fortest@yandex.ru"
toaddrs = "info@test.ru"

message = """To: %s
From: %s
Subject: Test Message

Hello,

This is a test message.
""" % (', '.join(toaddrs), fromaddr)

username = "iit.lectures"
password = getpass()

try:
    s = smtplib.SMTP(server)
    try:
        s.login(username, password)
    except smtplib.SMTPException, e:
        print "Authentication failed:", e
        sys.exit(1)
    s.sendmail(fromaddr, toaddrs, message)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
    print e
    sys.exit(2)
else:
    print "sent"
