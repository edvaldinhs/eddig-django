from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display="name","flips","time"
    
admin.site.register(Player,PlayerAdmin)