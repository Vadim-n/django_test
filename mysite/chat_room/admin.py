from django.contrib import admin
from chat_room.models import Room

class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ('creator', 'invited_users', 'date')

    def invited_users(self, obj):
        return "\n".join([user.invited_users for user in obj.room.all()])

admin.site.register(Room, RoomAdmin)