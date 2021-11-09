from django.conf import settings
from django.db import models

# Create your models here.
from client.models import Client


class EventStatus(models.Model):
    libelle = models.CharField(max_length=30)

class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    supportContact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    eventStatus = models.ForeignKey(to=EventStatus, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    eventDate = models.DateTimeField()
    note = models.CharField(max_length=20)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)