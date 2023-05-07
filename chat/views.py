from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Create your views here.
def index(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("chat_lobby",
                             {
                                 "type": "chat_message",
                                 "message": "Someone's here",
                                 "user": "System"
                             })
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})