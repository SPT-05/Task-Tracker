from django.urls import include, path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'tasktracker', views.TaskTrackerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]