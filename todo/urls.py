from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, LocationViewSet
from .tasks import scheduled_email_task

router = DefaultRouter()
router.register('locations', LocationViewSet, basename='location')
router.register('todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls))
]