from colorfield.fields import ColorField
from django.contrib.sites.models import Site
from django.db import models


# Create your models here.
class Label(Site):
    logo = models.ImageField()
    primary_color = ColorField()
    secondary_color = ColorField()
