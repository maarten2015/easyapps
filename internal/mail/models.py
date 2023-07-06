from django.db import models

from easyapps.utils import BaseModel

# Create your models here.


QUEUE_CHOICES = [("su", "Support"), ("sa", "Sales")]


class Accounts(BaseModel):
    name = models.CharField(max_length=255)
    queue = models.CharField(max_length=2, choices=QUEUE_CHOICES)
    host = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    secret_key_name = models.CharField(max_length=255, unique=True)


class Message(BaseModel):
    # From
    # In - Reply - To
    # Message - ID
    # Reply - To
    # Subject
    # Sender
    # To
    pass
