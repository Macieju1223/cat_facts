import time
import requests
import send_mail

def get_facts():
    print('localtime: ' + time.strftime('%H:%M:%S'))
    url = 'https://catfact.ninja/fact'
    req = requests.get(url)
    translate(req.json())

def translate(req):
    for key,value in req.items():
        if type(value) == dict:
            translate(value)
        else:
            return send_mail.Send_mail(key,value)