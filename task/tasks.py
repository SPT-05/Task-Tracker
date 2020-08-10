from __future__ import absolute_import, unicode_literals

from celery import shared_task
from task.models import Task, TaskTracker

from celery.schedules import crontab
from celery.decorators import periodic_task
import datetime


def get_single_day_tasks(task_type, day):
    return Task.objects.filter(task_type = task_type, create_at = day)

def get_single_week_tasks(task_type, day):
    start_date = day - datetime.timedelta(days = 7)
    return Task.objects.filter(created_at__range=[start_date, day])

def get_single_month_tasks(task_type, day):
    prev_month = day.month - 1
    cur_year = day.year
    return Task.objects.filter(created_at__month = prev_month, created_at__year = cur_year)

@periodic_task(run_every = (crontab(minute = 0, hour = '17', day_of_week = 'monday')), name = "weekly_task")
def send_email_weekly(email, task_type):
    today = datetime.date.today() 
    get_single_week_tasks(task_type, today)

@periodic_task(run_every = (crontab(minute = 0, hour = '17')), name = "daily_task")
def send_email_daily(email, task_type):
    today = datetime.date.today() 
    get_single_day_tasks(task_type, today)

@periodic_task(run_every = (crontab(minute = 0, hour = '17', day_of_month = '1')), name = "monthly_task")
def send_email_monthly(email, task_type):
    today = datetime.date.today() 
    get_single_month_tasks(task_type, today)
