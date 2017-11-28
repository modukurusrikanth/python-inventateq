#!/usr/bin/python

import smtplib

sender = 'modukuru.srikanth@gmail.com'
receivers = ['modukuru.srikanth@gmail.com']

message = """From: From Person <modukuru.srikanth@gmail.com>
To: To Person <modukuru.srikanth@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"