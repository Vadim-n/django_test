from rest_framework.views import APIView
from rest_framework.response import Response

from chat_room.models import Room, Chat
from chat_room.serializers import RoomSerializer, ChatSerializer

class Rooms(APIView):
    """Комната чата"""

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({"data": serializer.data})


class Dialog(APIView):
    """Диалог чата"""
    def get(self, request):
        room_id = request.get.data('room')
        chat = Chat.objects.filter(room=room_id)
        serializer = ChatSerializer(chat, many=True)
        return Response({'data': serializer.data})