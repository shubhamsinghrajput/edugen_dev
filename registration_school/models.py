from django.db import models
from django.template.loader import get_template
from django.core.mail import send_mail
import socket
import random


class RegistrationSchool(models.Model):
    USER_TYPE = (
        ('school', 'school'),
        ('authorised_person', 'Authorised Person'),
        ('owner_chairman', 'Owner/Chairman'),
        ('principal', 'Principal'),
    )
    school_name = models.CharField('School name', max_length=50)
    school_email = models.EmailField('School email', max_length=50)
    school_mobile_no = models.CharField('School mobile no', null=True, max_length=10)
    school_address = models.CharField('School address', max_length=50)
    cid = models.CharField('CID', max_length=50)
    user_type = models.CharField('User type', choices=USER_TYPE, max_length=50)
    mobile_confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = "School registration"
        verbose_name_plural = "school registration"

    def __str__(self):
        return self.school_name

    def save(self, *args, **kwargs):
        if self.pk is None:
            characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
            result = ''
            for i in range(0, 20):
                result += random.choice(characters)

            self.cid = result

            subject = 'Registered in Edugen portal'
            message = get_template('registration_school_email.html').render(
                {
                    # 'link': socket.gethostbyname(socket.gethostname()),
                    'link': '192.168.1.215',
                    'cid': self.cid
                }
            )

            send_mail(subject, message, self.school_email, [self.school_email], html_message=message,
                      fail_silently=True)
        super(RegistrationSchool, self).save(*args, **kwargs)
