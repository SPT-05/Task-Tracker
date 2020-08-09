from django.contrib import admin
from .models import TaskTracker, Task
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskTracker)
