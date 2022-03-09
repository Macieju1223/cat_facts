from json import load
from dotenv import load_dotenv
import smtplib
import os
import mails

load_dotenv()

def Send_mail(title,content):

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(os.getenv('MAIL_ADDR'),os.getenv('PASSWORD'))

        mail_content = f'Subject: {title}\n{content}'
        print(f"{mail_content}\n--------------------")
        for mail in mails.mail_list:
            try:
                #smtp.sendmail(os.getenv('MAIL_ADDR'),mail,mail_content)
                print(f'Mail to {mail} sent..')
            except:
                print(f"mail to {mail} error occured")
                pass
        smtp.quit()
