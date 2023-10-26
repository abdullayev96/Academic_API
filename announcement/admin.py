from django.contrib import admin
from .models import Message



class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'body', 'image', 'created_at')

    list_filter = ('id','name',)
    search_fields = ("name")


admin.site.register(Message, MessageAdmin)


