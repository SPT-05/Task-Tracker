from rest_framework import serializers
from task.models import Task,TaskTracker

class TaskSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_type', 'task_desc','created_at']

class TaskTrackerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskTracker
        fields = ['id', 'task_type', 'update_type', 'email']