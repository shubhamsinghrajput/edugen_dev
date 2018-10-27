from django.contrib import admin
from .models import RegistrationSchool


class RegistrationSchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'school_email', 'school_mobile_no',
                    'school_address']
    list_filter = ('school_name', 'school_email', 'school_mobile_no', 'school_address')
    exclude = ("cid ",)
    readonly_fields = ('cid', 'mobile_confirm',)


admin.site.register(RegistrationSchool, RegistrationSchoolAdmin)
