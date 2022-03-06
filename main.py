from dotenv import load_dotenv
import time
from threading import Timer
import requests
import json
import smtplib
import os
from mails import mail_list
from email.mime.text import MIMEText

load_dotenv()

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)

def send_mail(title,content):
    
    addr = os.getenv('MAIL_ADDR')
    passwd = os.getenv('PASSWORD')

    with smtplib.SMTP('smtp.gmail.com',587) as smtp: # 587 - SMTP port
        smtp.ehlo() # - identyfies ourself with mail server that im using
        smtp.starttls() # - encypting trafic
        smtp.ehlo() # - re run ehlo to reidentyfie ourself as encrypted msg
        smtp.login(os.getenv('MAIL_ADDR'),os.getenv('PASSWORD'))

        mail_content = f'Subject: {title}\n{content}'
        print(mail_content)
        for mail in mail_list:
            try:
                smtp.sendmail(addr,mail,mail_content) # - sender addr,reciver addr,msg
                print(f"Mail to {mail} sent...")
            except:
                print(f"{mail} Error occured")
                pass
        print('---------------------------------------------')

def get_facts(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))
    url = os.getenv('API_URL')
    req = requests.get(url)
    translate(req.json())

def translate(facts):
    for key,value in facts.items():
        if type(value) == dict:
            translate(value)
        else:
            return send_mail(key,value)

if __name__ == '__main__':
    timer = RepeatTimer(10,get_facts,['Local Timme: '])  # --- ([1s],[cals function],[str[list]]
    timer.start() # --- call 'run' from 'void'
    print('Threding strated...')
