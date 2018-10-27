from django import forms
from .models import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = RegistrationTeacher
        exclude = ('teacher_token', 'email_confirm', 'mobile_confirm')
