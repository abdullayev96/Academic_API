from django.contrib import admin
from .models import Chair


class ChairAdmin(admin.ModelAdmin):
    list_display = ('id','chair_name', 'chair_full', 'chair_result','image', 'title','created_at')

    list_filter = ('id','chair_name','chair_full')
    search_fields = ("chair_name", 'chair_full')


admin.site.register(Chair, ChairAdmin)

