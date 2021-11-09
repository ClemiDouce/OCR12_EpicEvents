from django.contrib import admin
from django import forms

# Register your models here.
from userteam.models import Employe, Team


admin.site.register(Team)

class UserForm(forms.ModelForm):
    class Meta:
        fields = ["first_name", "last_name", "username", "email", "password", "team"]

@admin.register(Employe)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
