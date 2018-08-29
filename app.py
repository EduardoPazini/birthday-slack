from datetime import datetime
from requests import post

from apscheduler.schedulers.blocking import BlockingScheduler


SLACK_URL = "https://slack.com/api/chat.postMessage"
HEADER = {
        "Authorization": "Bearer xoxp-120107970803-391446038516-421372942080-5da47da3a5fc742ed296bf0541d0b9fe"
}
BIRTHS = {
    "Murilo": "8/15/1999",
    "Carlos": "8/23/2018",
    "Daniel": "2/2/2018"
}


def formatMessage(nome):
    message = {
        "channel": "UBHD414F6",
        "text": "FELIZ ANIVERSÁRIO, {}!!!".format(nome)
    }

    return message


def isSomeoneBirthday():
    utc_date = datetime.now()
    today = ("{}/{}/{}").format(utc_date.month, utc_date.day, utc_date.year)

    for data in BIRTHS.items():
        if today == data[1]:
            post(SLACK_URL, json=formatMessage(data[0]), headers=HEADER)
    
    return "Ninguém faz aniversário hoje :/"


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=8)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
    isSomeoneBirthday()


@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')


sched.start()