import time
from threading import Timer
import requests
import json
import smtplib

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)
def send_mail(title,content):
    
    addr = ''
    passwd = ''

    with smtplib.SMTP('smtp.gmail.com',587) as smtp: # 587 - SMTP port
        smtp.ehlo() # - identyfies ourself with mail server that im using
        smtp.starttls() # - encypting trafic
        smtp.ehlo() # - re run ehlo to reidentyfie ourself as encrypted msg
        smtp.login(addr,passwd)

        mail = f'Subject: {title}\n{content}'
        try:
            smtp.sendmail(addr,'',mail) # - sender addr,reciver addr,msg
            print('Mail sent')
        except:
            pass

def get_facts(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))
    url = 'https://catfact.ninja/fact'
    req = requests.get(url)
    translate(req.json())

def translate(facts):
    for key,value in facts.items():
        if type(value) == dict:
            translate(value)
        else:
            print(key, ':', value)
            return send_mail(key,value)

if __name__ == '__main__':
    timer = RepeatTimer(10,get_facts,['Local Timme: '])  # --- ([1s],[cals function],[str[list]]
    timer.start() # --- call 'run' from 'void'
    print('threding strated')
    # have to suspend execution of current thread, otherwise its gonna blow :(
    time.sleep(20) # -- sleeps main program for 10s but function works in background

