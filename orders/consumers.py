import json
from channels.generic.websocket import WebsocketConsumer
from .models import Order
from asgiref.sync import async_to_sync


class OrderConsumer(WebsocketConsumer):
    def connect(self):
        self.room = 'orders'
        async_to_sync(self.channel_layer.group_add)(self.room, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room, self.channel_name)

    def recieve(self, text_data):
        data = json.loads(text_data)
        action = data['action']
        if action == 'create_order':
            order = Order.objects.create(details=data['message'], taker=self.scope['user'])


        elif action == 'fulfill_order':
            order = Order.objects.get(unique_number=data['number'])
            order.fulfilled = True
            order.fulfilled_by = self.scope['user']
            order.save()

        async_to_sync(self.channel_layer.group_send)(self.room,
                                                     {'type': 'order_update',
                                                      'data': {
                                                          'action': action,
                                                          'order_number': order.unique_number,
                                                          'order_content': order.details,
                                                          'order_taken_by': order.taker,
                                                          'order_fulfilled': order.fulfilled,
                                                          'order_fulfilled_by': order.fulfilled_by,
                                                          'order_created': order.created.iso_format()

                                                      },
                                                      },
                                                     )

    def order_update(self, event):
        data = event["data"]
        self.send(text_data=json.dumps(data))
