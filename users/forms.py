from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")
