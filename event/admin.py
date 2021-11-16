from django.contrib import admin

# Register your models here.
from event.models import Event, EventStatus

admin.site.register(EventStatus)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'supportContact', 'eventStatus', 'attendees', 'eventDate', 'note')
