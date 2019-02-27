from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyCustomUserCreationForm, MyCustomUserChangeForm
from .models import MyCustomUser


# Register your models here.
class MyCustomUserAdmin(UserAdmin):
    model = MyCustomUser
    add_form = MyCustomUserCreationForm
    form = MyCustomUserChangeForm


admin.site.register(MyCustomUser, MyCustomUserAdmin)
