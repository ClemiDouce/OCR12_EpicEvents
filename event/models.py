from django.db import models

# Create your models here.
from client.models import Client


class EventStatus(models.Model):
    libelle = models.CharField(max_length=30)

class Event(models.Model):
    client = models.ForeignKey(to=Client)
    supportContact = models.ForeignKey(to=Employe)
    eventStatus = models.ForeignKey(to=EventStatus)
    attendees = models.IntegerField()
    eventDate = models.DateTimeField()
    note = models.CharField(max_length=20)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)