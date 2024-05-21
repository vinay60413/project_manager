import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage, Task
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.task_id = self.scope['url_route']['kwargs']['task_id']
        self.task_group_name = f'chat_{self.task_id}'

        await self.channel_layer.group_add(
            self.task_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.task_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        task = await Task.objects.get(id=self.task_id)
        user = await User.objects.get(username=username)
        chat_message = ChatMessage.objects.create(task=task, user=user, message=message)

        await self.channel_layer.group_send(
            self.task_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
