from django.contrib import admin

# Register your models here.
from event.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client', 'supportContact', 'eventStatus', 'attendees', 'eventDate', 'note')