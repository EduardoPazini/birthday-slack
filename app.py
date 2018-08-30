from datetime import datetime
from requests import post
#import birthday_register

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

#SLACK_URL = "https://slack.com/api/chat.postMessage"
HEADER = {
        "Authorization": ""
}
BIRTHS = {
    "Murilo": "8/15/1999",
    "Carlos": "8/29/2018",
    "Daniel": "2/2/2018"
}


def formatMessage(nome):
    message = {
        "channel": "",
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


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=19)
def scheduled_job():
    print('This job is run every weekday at 19pm.')
    isSomeoneBirthday()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every one minute.')
    isSomeoneBirthday()

sched.start()