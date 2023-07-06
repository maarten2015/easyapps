from django.core.management.base import BaseCommand
from imap_tools import MailBox


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):

        with MailBox("pro1.mail.ovh.net").login(
            "support@ideeenbox.nl", "ktq.XFE6wpn1duc!bvk"
        ) as mailbox:
            for msg in mailbox.fetch(criteria="UNSEEN"):
                print(msg.uid)  # str | None: '123'
                print(msg.subject)  # str: 'some subject 你 привет'
                print(msg.from_)  # str: 'Bartölke@ya.ru'
                print(msg.to)  # tuple: ('iam@goo.ru', 'friend@ya.ru', )
                print(msg.cc)  # tuple: ('cc@mail.ru', )
                print(msg.bcc)  # tuple: ('bcc@mail.ru', )
                print(msg.reply_to)  # tuple: ('reply_to@mail.ru', )
                print(
                    msg.date
                )  # datetime.datetime: 1900-1-1 for unparsed, may be naive or with tzinfo
                print(
                    msg.date_str
                )  # str: original date - 'Tue, 03 Jan 2017 22:26:59 +0500'
                print(msg.text)  # str: 'Hello 你 Привет'
                print(msg.html)  # str: '<b>Hello 你 Привет</b>'
                print(msg.flags)  # tuple: ('\\Seen', '\\Flagged', 'ENCRYPTED')
                print(
                    msg.headers
                )  # dict: {'received': ('from 1.m.ru', 'from 2.m.ru'), 'anti-virus': ('Clean',)}
                print(
                    msg.size_rfc822
                )  # int: 20664 bytes - size info from server (*useful with headers_only arg)
                print(msg.size)  # int: 20377 bytes - size of received message

                for att in msg.attachments:  # list: imap_tools.MailAttachment
                    print(att.filename)  # str: 'cat.jpg'
                    print(att.payload)  # bytes: b'\xff\xd8\xff\xe0\'
                    print(att.content_id)  # str: 'part45.06020801.00060008@mail.ru'
                    print(att.content_type)  # str: 'image/jpeg'
                    print(att.content_disposition)  # str: 'inline'
                    print(att.part)  # email.message.Message: original object
                    print(att.size)  # int: 17361 bytes
