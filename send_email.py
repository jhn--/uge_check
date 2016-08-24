#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

recipients = ['user1@example.com', 'user2@example.com']
sender = 'sender@example.com'

datetimenow = str(datetime.datetime.now())
msg = MIMEMultipart('alternative')
msg['From'] = sender
msg['To'] = ", ".join(recipients)


def ooc_email():
    msg['Subject'] = "Nodes down at {0}".format(datetimenow)

    nooc = '/var/www/html/initializr/nodes_out_of_circulation.html'

    try:
        nooc_fp =  open(nooc, 'r')
    except Exception, e:
        print(e)
    else:
        html_source = "\n".join(line for line in nooc_fp.readlines())
    finally:
        nooc_fp.close()

    html_msg = MIMEText(html_source, 'html')
    msg.attach(html_msg)

    smtpserver = smtplib.SMTP('localhost')
    smtpserver.sendmail(sender, recipients, msg.as_string())
    smtpserver.quit()

def main():
    print("Not supposed to run this script as is.")

if __name__ == '__main__':
    main()
