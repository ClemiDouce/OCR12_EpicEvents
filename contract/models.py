from django.conf import settings
from django.db import models

# Create your models here.
from client.models import Client


class Contract(models.Model):
    saleContact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    amount = models.FloatField()
    paymentDue = models.DateTimeField()

    def __str__(self):
        return f"{self.client} {self.saleContact}"

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"
        ordering = ['dateCreated']