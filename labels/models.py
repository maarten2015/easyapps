from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    logo = models.ImageField()
    primary_color = ColorField()
    secondary_color = ColorField()
