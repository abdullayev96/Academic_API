from django.contrib import admin
from .models import Leader



class LeaderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'image','email', 'number', 'phone', ' rest', 'created_at')

    list_filter = ('full_name',)
    search_fields = ("id","full_name")


admin.site.register(Leader, LeaderAdmin)

