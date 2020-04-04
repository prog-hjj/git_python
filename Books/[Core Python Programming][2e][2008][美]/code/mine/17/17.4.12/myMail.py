#!/usr/bin/env python

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'smtp.163.com'
POP3SVR = 'pop.163.com'

print 'This program send an email of 163.com to yourself.'
name = raw_input('Enter name: ')
pwd = raw_input('Enter password: ')

addr = '%s@163.com' % name

origHdrs = ['From: %s' % addr,
            'To: %s' % addr,
            'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
sendSvr.login(addr, pwd)
errs = sendSvr.sendmail(addr, (addr,), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)  # wait for mail to be delivered

recvSvr = POP3(POP3SVR)
recvSvr.user(name)
recvSvr.pass_(pwd)
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody == recvBody  # assert identical
print 'DONE'
