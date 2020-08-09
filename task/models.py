from django.db import models

# Create your models here.

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

