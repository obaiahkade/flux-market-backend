import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "logs"
        # లాగ్స్ గ్రూప్‌లోకి కనెక్ట్ అవ్వడం
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # గ్రూప్ నుండి డిస్‌కనెక్ట్ అవ్వడం
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def log_message(self, event):
     
        data = event['data']
        await self.send(text_data=json.dumps(data))