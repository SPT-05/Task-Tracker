from __future__ import absolute_import, unicode_literals

from celery import shared_task
from task.models import Task, TaskTracker

from celery.schedules import crontab

import datetime


def get_single_day_tasks(task_type, day):
    return Task.objects.filter(task_type = task_type, create_at = day)

def get_single_week_tasks(task_type, day):
    week_tasks = []
    for i in range(7):
        cur_date = day - datetime.timedelta(days = i)
        week_tasks.append(get_single_day_tasks(task_type, cur_date))
    return week_tasks

def get_single_month_tasks(task_type, day):
    month_tasks = []
    for i in range(4):
        cur_week = day - datetime.timedelta(weeks = i)
        month_tasks.append(get_single_week_tasks(task_type, cur_week))
    return month_tasks

def sent_email(email, update_type, task_type):
    today = datetime.date.today() 
    if(update_type == "1"):
        get_single_week_tasks(task_type, today)
    elif(update_type == "2"):
        get_single_day_tasks(task_type, today)
    elif(update_type == "3"):
        get_single_month_tasks(task_type, today)
