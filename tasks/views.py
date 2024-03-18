from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse


def home(request):
    return HttpResponse("Benteler Task Manager") 

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()

        # Send a message over the WebSocket connection
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'tasks',  # This should match the group name in your consumer
            {
                'type': 'task.created',
                'task': {
                    'id': task.id,
                    'title': task.title,
                    'description': task.description,
                    'completed': task.completed,
                    # ... any other task fields you want to include ...
                },
            }
        )

def select_task(request, task_id):
    # ... code to select the task ...

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('tasks', {
        'type': 'task_selected',
        'task_id': task_id,
        'username': request.user.username,
    })