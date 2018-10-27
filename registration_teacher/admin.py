from django.contrib import admin
from .models import *


class RegistrationTeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'teacher_email', 'teacher_subject']
    list_filter = ('teacher_name', 'teacher_email', 'teacher_subject')
    readonly_fields = ('email_confirm', 'mobile_confirm',)


admin.site.register(RegistrationTeacher, RegistrationTeacherAdmin)
