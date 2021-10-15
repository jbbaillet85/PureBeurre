from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return f"{self.last_name}"
