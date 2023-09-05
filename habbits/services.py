import requests
from habbits.models import Habbit
from users.models import Users
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from config import settings

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN


def habbit_scheduler() -> None:
    current_time = datetime.now()
    for habbit in Habbit.objects.filter(is_pleasant=False):

        if habbit.frequency == "DAILY":
            if habbit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                print(f'HABIT INFORMATION: {habbit}')
                chat_id = habbit.owner.chat_id
                if habbit.award:
                    message = f"ACTION: {habbit.action}\nPLACE: {habbit.place}\nYOUR AWARD: {habbit.award}\nDURATION: {habbit.duration}"
                else:
                    message = f"ACTION: {habbit.action}\nPLACE: {habbit.place}\nMAKE PLEASANT HABIT: {habbit.link_pleasant.action}\nDURATION: {habbit.duration}"
                url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url)

        else:
            today = ""
            # check current day
            if datetime.today().weekday() == 0:
                today = "MONDAY"
            elif datetime.today().weekday() == 1:
                today = "TUESDAY"
            elif datetime.today().weekday() == 2:
                today = "WEDNESDAY"
            elif datetime.today().weekday() == 3:
                today = "THURSDAY"
            elif datetime.today().weekday() == 4:
                today = "FRIDAY"
            elif datetime.today().weekday() == 5:
                today = "SATURDAY"
            elif datetime.today().weekday() == 6:
                today = "SUNDAY"

            if habbit.frequency == today:
                if habbit.time.strftime("%H:%M") == current_time.strftime("%H:%M"):
                    print(f'HABIT INFORMATION: {habbit}')
                    chat_id = habbit.owner.chat_id
                    if habbit.award:
                        message = (
                            f"ACTION: {habbit.action}\nPLACE: {habbit.place}\nYOUR AWARD: {habbit.award}\nDURATION: "
                            f"{habbit.duration}")
                    else:
                        message = (f"ACTION: {habbit.action}\nPLACE: {habbit.place}\nMAKE PLEASANT HABIT:"
                                   f" {habbit.link_pleasant.action}\nDURATION: {habbit.duration}")

                    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                    requests.get(url)


def telegram_check_updates() -> None:
    """ get information from telegram bot and add user telegram id to base"""
    url_get_updates = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    response = requests.get(url_get_updates)
    if response.status_code == 200:
        for telegram_users in response.json()["result"]:
            telegram_user_chat_id = telegram_users["message"]["from"]["id"]
            telegram_user_name = telegram_users["message"]["from"]["username"]

            try:
                user = Users.objects.get(telegram_user_name=telegram_user_name)
                if user.chat_id is None:
                    user.chat_id = telegram_user_chat_id
                    user.save()
            except ObjectDoesNotExist:
                print("No user in the bases.")
