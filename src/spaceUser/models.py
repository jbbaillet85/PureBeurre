from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self) -> str:
        return f"{self.last_name}"
