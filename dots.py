import os
import time
def clear():
    clear = lambda: os.system('clear')
    clear()

def dotss():
    for i in range(10):
        string = 'Working' + '.' * i
        print('\033[k',string, end='\r')
        time.sleep(0.5)