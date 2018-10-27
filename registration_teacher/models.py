from django.db import models
from django.template.loader import get_template
from chapter.models import classes, Subject
from django.core.mail import send_mail
from registration_school.models import RegistrationSchool
import socket
import random


class RegistrationTeacher(models.Model):
    TEACHER_SUBJECT = (
        ('science', 'Science'),
    )

    teacher_name = models.CharField('Teacher name', max_length=50)
    teacher_email = models.EmailField('Teacher email', max_length=50)
    teacher_mobile_no = models.CharField('Teacher mobile no', max_length=10)
    school_name = models.ForeignKey(RegistrationSchool, on_delete=models.CASCADE)
    teacher_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_token = models.CharField('Token', max_length=50)
    classes = models.ManyToManyField(classes)
    email_confirm = models.BooleanField(default=False)
    mobile_confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Teacher registration"
        verbose_name_plural = "Teacher registration"

    def __str__(self):
        return self.teacher_name

    def save(self, *args, **kwargs):
        if self.pk is None:
            characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
            result = ''
            for i in range(0, 20):
                result += random.choice(characters)

            self.token = result

            subject = 'Email verified for Edugen'
            message = get_template('email_verified.html').render(
                {
                    # 'link': socket.gethostbyname(socket.gethostname()),
                    'link': '192.168.1.215',
                    'token': self.token
                }
            )

            send_mail(subject, message, self.teacher_email, [self.teacher_email], html_message=message,
                      fail_silently=True)

            self.teacher_token = self.token
            self.email_confirm = False
            self.mobile_confirm = False
        super(RegistrationTeacher, self).save(*args, **kwargs)
