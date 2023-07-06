from django.db import models

from easyapps.utils import BaseModel
from internal.labels.models import Label
from internal.mail import Message

TICKET_STATUSES = [("ne", "New"), ("pe", "Pending"), ("cl", "Closed")]
TICKET_SOURCES = [("em", "Email"), ("po", "Portal")]
# Create your models here.


class Ticket(BaseModel):
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
    subject = models.CharField(max_length=255)
    status = models.CharField(max_length=2, choices=TICKET_STATUSES)


class Comment(BaseModel):
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    source = models.CharField(max_length=2, choices=TICKET_SOURCES)
    raw_email = models.ForeignKey(Message, on_delete=models.PROTECT, null=True)
    internal = models.BooleanField()


class TicketAttachments(BaseModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
