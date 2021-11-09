from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)


class Employe(AbstractUser):
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)