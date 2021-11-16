from django import forms
from django.contrib import admin

# Register your models here.
from userteam.models import Employe, Team

admin.site.register(Team)


class UserForm(forms.ModelForm):
    class Meta:
        fields = ["first_name", "last_name", "username", "email", "password", "team", "is_staff"]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        # user.set_password(self.cleaned_data["password"])
        user.is_superuser = self.cleaned_data['is_staff']
        if commit:
            user.save()
        return user


@admin.register(Employe)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
