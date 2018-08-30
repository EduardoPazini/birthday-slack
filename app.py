from datetime import datetime
from requests import post

# import birthday_register
from dotenv import load_dotenv
import os

from apscheduler.schedulers.blocking import BlockingScheduler

load_dotenv()

HEADER = {"Authorization": os.getenv("TOKEN")}
BIRTHS = {"Murilo": "8/15/1999", "Carlos": "8/29/2018", "Daniel": "2/2/2018"}


def formatMessage(nome):
    message = {
        "channel": os.getenv("CHANNEL"),
        "text": "FELIZ ANIVERSÁRIO, {}!!!".format(nome),
    }

    return message


def isSomeoneBirthday():
    utc_date = datetime.now()
    today = ("{}/{}/{}").format(utc_date.month, utc_date.day, utc_date.year)

    for data in BIRTHS.items():
        if today == data[1]:
            post(os.getenv("SLACK_URL"), json=formatMessage(data[0]), headers=HEADER)

    return "Ninguém faz aniversário hoje :/"


sched = BlockingScheduler()


@sched.scheduled_job("cron", day_of_week="mon-fri", hour=19)
def scheduled_job():
    print("This job is run every weekday at 19pm.")
    isSomeoneBirthday()


@sched.scheduled_job("interval", minutes=1)
def timed_job():
    print("This job is run every one minute.")
    isSomeoneBirthday()


sched.start()
