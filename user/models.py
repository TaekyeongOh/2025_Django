from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    nickname=models.CharField(max_length=30)

    groups=models.ManyToManyField(Group, related_name="customer_set", blank=True)
    user_permissions= models.ManyToManyField(Permission, related_name="customer_permissions_set", blank=True)
