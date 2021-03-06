from django.conf import settings
from django.db import models

# Create your models here.
from client.models import Client


class EventStatus(models.Model):
    libelle = models.CharField(max_length=30)

    def __str__(self):
        return self.libelle

    class Meta:
        verbose_name = "EventStatus"
        verbose_name_plural = "EventStatus"


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True)
    supportContact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    eventStatus = models.ForeignKey(to=EventStatus, on_delete=models.CASCADE, default=1)
    attendees = models.IntegerField()
    eventDate = models.DateTimeField()
    note = models.CharField(max_length=20, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} {self.supportContact}"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['eventDate']
