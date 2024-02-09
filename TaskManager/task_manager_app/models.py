from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title