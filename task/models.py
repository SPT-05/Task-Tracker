from django.db import models
from celery.schedules import crontab
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_email_weekly, send_email_monthly, send_email_daily

type_choices = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4")
)
# Task.objects.all().filter(created_at__month = 7)
class Task(models.Model):
    task_type = models.CharField(max_length=1, choices=type_choices, default="1")
    task_desc = models.CharField(max_length = 300)
    created_at = models.DateField(editable = False)

class TaskTracker(models.Model):
    task_type = models.CharField(max_length=1, choices=type_choices, default="1")
    
    # update_type signifies 
    # 1 -> Weekly 
    # 2 -> Daily 
    # 3 -> Monthly
    update_choices = (
        ("1", "Weekly"),
        ("2", "Daily"),
        ("3", "Monthly")
    )
    #Default Update is Daily
    update_type = models.CharField(max_length=1, choices=update_choices, default="1")

    email = models.EmailField(max_length = 30)

@receiver(post_save, sender=TaskTracker, dispatch_uid="create_celery_task")
def create_celery(sender, instance, **kwargs):
    if(instance.update_choices == "1"):
        send_email_weekly.delay(instance.email, instance.task_type)
    elif(instance.update_choices == "2"):
        send_email_daily.delay(instance.email, instance.task_type)
    elif(instance.update_choices == "3"):
        send_email_weekly.delay(instance.email, instance.task_type)