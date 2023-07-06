from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.sites.models import Site
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from easyapps.utils import BaseModel


# Create your models here.
class Customer(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class Contact(AbstractUser, BaseModel):
    company = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.PROTECT
    )
    email = models.EmailField(max_length=255, unique=True)
    phone = PhoneNumberField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


class Notes(BaseModel):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    author = models.ForeignKey(
        Contact,
        related_name="notes_written",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    deleted = models.BooleanField()
    text = models.TextField()


class Ticket(BaseModel):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)


class Comment(BaseModel):
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)


class Event(BaseModel):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True)
    anonymousID = models.UUIDField(blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    event = models.CharField(max_length=200)
    properties = models.JSONField()


class Visit(BaseModel):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True)
    anonymousID = models.UUIDField(blank=True, null=True)
    fingerprint = models.CharField(max_length=255, blank=True, null=True)
    # is_mobile
    # is_tablet
    # is_touch_capable
    # is_pc
    # is_bot
    # browser_family
    # browser_version
    # os_family
    # os_version
    # device_family
    # user_agent
    # ip_address
    # city
    # continent_code
    # continent_name
    # country_code
    # country_name
    # dma_code
    # is_in_european_union
    # latitude
    # longitude
    # postal_code
    # region
    # time_zone

    class Meta:
        indexes = [
            models.Index(fields=["fingerprint"]),
            models.Index(fields=["anonymousID"]),
        ]


class PageView(BaseModel):
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
