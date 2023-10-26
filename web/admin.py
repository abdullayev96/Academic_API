from django.contrib import admin
from .models import Users, Images


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','teacher', 'student', 'otm', 'acceptance')

    list_filter = ('id','student',)
    search_fields = ("teacher", )


admin.site.register(Users, UsersAdmin)
admin.site.register(Images)
