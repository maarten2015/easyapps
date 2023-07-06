from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from internal.crm.models import Contact


@admin.register(Contact)
class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {PhoneNumberField: {"widget": PhoneNumberPrefixWidget}}
