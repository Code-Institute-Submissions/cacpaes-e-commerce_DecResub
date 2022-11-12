from django.db import models
from django.contrib.auth.models import User

class SubscribedUsers(models.Model):
    """ Entity to subcribed users to newsleatter"""
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user", null=True
        )