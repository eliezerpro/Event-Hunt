from django.contrib import admin
from .models import EventLocation, EventManager

# Register your models here.

class EventManagerAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'post_date']

class EventLocationAdmin(admin.ModelAdmin):
    list_display = ['title','address', 'zip_code', 'city', 'states']

admin.site.register(EventManager, EventManagerAdmin)
admin.site.register(EventLocation, EventLocationAdmin)