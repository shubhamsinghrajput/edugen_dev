from django.contrib import admin
from .models import *

admin.site.register(classes)
admin.site.register(Subject)
admin.site.register(Chapter)


class UnitWithChaptersAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'subject', 'chapter_name', 'unit_name', 'chapter_no']
    list_filter = ('class_name', 'subject')


admin.site.register(UnitWithChapters, UnitWithChaptersAdmin)


class LessonPlanAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'subject', 'chapter_no']
    list_filter = ('class_name', 'subject')


admin.site.register(LessonPlan, LessonPlanAdmin)


class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['question_no', 'question', 'category', 'question_type']
    list_filter = ('category', 'question_type')


admin.site.register(QuestionBank, QuestionBankAdmin)


class BrainStormAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'subject', 'chapter_no', 'name']
    list_filter = ('class_name', 'subject', 'chapter_no')


admin.site.register(BrainStorm, BrainStormAdmin)


class TellYourTeacherAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'subject', 'chapter_no', 'name']
    list_filter = ('class_name', 'subject', 'chapter_no')


admin.site.register(TellYourTeacher, TellYourTeacherAdmin)


class FindOutAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'subject', 'chapter_no', 'name']
    list_filter = ('class_name', 'subject', 'chapter_no')


admin.site.register(FindOut, FindOutAdmin)


class WordSearchAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'subject', 'chapter_no', 'image_tag']
    list_filter = ('class_name', 'subject', 'chapter_no')


admin.site.register(WordSearch, WordSearchAdmin)
