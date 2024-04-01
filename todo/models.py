from django.db import models
from django.contrib.auth.models import User
# default, unique, blank(input-form), null(database)
class Todo(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    time = models.TimeField(default='00:00')
    date = models.DateField()
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True, related_name='todos')
    participants = models.ManyToManyField(User, blank=True, related_name='participated_todos')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_todos')
# 顯示時更簡單明瞭
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name