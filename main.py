import schedule
import Get_cat_facts
import dots
import time


def job_todo():
    Get_cat_facts.get_facts()
    dots.dotss()

schedule.every().day.at('07:00').do(job_todo)

if __name__ == '__main__':
    print('schedule startet ad ',time.strftime('%H:%M:%S'))
    while True:
        schedule.run_pending()