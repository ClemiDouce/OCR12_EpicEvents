from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employe(AbstractUser):
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.team}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['last_name']

    def get_team_name(self):
        return self.team.name.lower()
