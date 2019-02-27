from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyCustomUser


class MyCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyCustomUser
        fields = UserCreationForm.Meta.fields


class MyCustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyCustomUser
        fields = UserChangeForm.Meta.fields
