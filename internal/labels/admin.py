from django.contrib import admin
from django.contrib.sites.models import Site

from .models import Label

# Register your models here.
admin.site.register(Label)
admin.site.unregister(Site)
