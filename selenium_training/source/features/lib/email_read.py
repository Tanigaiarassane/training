

import smtplib
import time
import imaplib
import email
import re
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
USER_NAME = ""
PASSWORD = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(USER_NAME,PASSWORD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        first_email_id  = latest_email_id- 100
        print first_email_id
        print range(latest_email_id, first_email_id, -1)
        for i in range(latest_email_id,first_email_id, -1):
            type, data = mail.fetch(i, '(RFC822)' )
            print id
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    if "Verify your identity in Salesforce" in email_subject:
                        code =  re.search("(Verification Code: )([\d]+)",str(msg.get_payload()))
                        return code.group(2)
    except Exception, e:
        print str(e)

if __name__ == "__main__":
    print "code : " + read_email_from_gmail()
