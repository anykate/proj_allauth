from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class MyCustomUserManager(UserManager):
    pass


class MyCustomUser(AbstractUser):
    objects = MyCustomUserManager()
