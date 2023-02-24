from django.contrib import admin
from .models import WorkExample, Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','project_name']

admin.site.register(WorkExample)
admin.site.register(Client, ClientAdmin)
