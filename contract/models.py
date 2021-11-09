from django.conf import settings
from django.db import models

# Create your models here.
from client.models import Client


class Contract(models.Model):
    saleContact = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    client = models.ForeignKey(to=Client)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    amount = models.FloatField()
    paymentDue = models.DateTimeField()