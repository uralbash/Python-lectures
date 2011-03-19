import getpass, poplib, sys

host = "pop.yandex.ru"
user = "fortest@yandex.ru"
passwd = getpass.getpass()

p = poplib.POP3(host)
try:
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto, e:
    print "Login failed:", e
    sys.exit(1)
status = p.stat()
print "Mailbox has %d messages for a total of %d bytes" % (status[0], status[1])
for item in p.list()[1]:
    number, octets = item.split(' ')
    print "Message %s: %s bytes" % (number, octets)
p.quit()
