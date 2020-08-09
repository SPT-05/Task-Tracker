from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer, TaskTrackerSerializer
from .models import Task, TaskTracker

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

class TaskTrackerViewSet(viewsets.ModelViewSet):
    queryset = TaskTracker.objects.all().order_by('id')
    serializer_class = TaskTrackerSerializer