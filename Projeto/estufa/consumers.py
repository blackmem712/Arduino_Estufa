import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import SensorData

class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        latest_data = SensorData.objects.latest('timestamp')
        data = {
            'umidade': latest_data.umidade,
            'temperatura': latest_data.temperatura,
            'timestamp': latest_data.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
        await self.send(text_data=json.dumps(data))