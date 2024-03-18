from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to the current time when the task is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set to the current time whenever the task is updated
    created_by = models.CharField(max_length=200)  # The username of the user who created the task
    completed_by = models.CharField(max_length=200, null=True, blank=True)  # The username of the user who completed the task
    is_selected = models.BooleanField(default=False)  # Indicates whether the task is selected
    selected_by = models.CharField(max_length=200, null=True, blank=True)  # The username of the user who selected the task