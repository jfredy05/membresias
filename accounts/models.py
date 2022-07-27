from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Extends Django User

    Args:
        AbstractUser (_type_): User
    """
    stripe_customer_id = models.CharField(max_length=50)
