from celery import shared_task
from habbits.services import telegram_check_updates, habbit_scheduler


@shared_task(name="check_habit_time")
def check_habit_time():

    telegram_check_updates()
    habbit_scheduler()
