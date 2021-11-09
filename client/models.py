from django.conf import settings
from django.db import models

# Create your models here.
class Client(models.Model):
    firstName = models.CharField(max_length=25)
    salesContact = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    lastName = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    companyName = models.CharField(max_length=250)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now_add=True)