from django.contrib import admin
from .models import User,Calendar,Event,Invites


admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(Invites)
