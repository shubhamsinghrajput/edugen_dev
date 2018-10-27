from django.db import models
from django.utils.html import format_html


class classes(models.Model):
    classes = models.CharField('Class', max_length=50)

    def __str__(self):
        return self.classes


class Chapter(models.Model):
    chapter_no = models.CharField('Chapter No', max_length=500)

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"

    def __str__(self):
        return self.chapter_no


class Subject(models.Model):
    subject = models.CharField('Subject', max_length=50)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.subject


class AbstractData(models.Model):
    TEACHER_SUBJECT = (
        ('science', 'Science'),
    )
    class_name = models.ForeignKey(classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter_no = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class UnitWithChapters(AbstractData):
    unit_name = models.CharField('Unit name', max_length=50)
    chapter_name = models.CharField('Chapter name', max_length=500)

    class Meta:
        verbose_name = "Chapter With Unit"
        verbose_name_plural = "Chapter With Unit"

    def __str__(self):
        return self.chapter_name


class LessonPlan(AbstractData):
    goal = models.TextField('Goal')
    objective = models.TextField('Objective')
    teaching_aids = models.TextField('Teaching Aids')
    teaching_seggestions = models.TextField('Teaching suggestions')

    class Meta:
        verbose_name = "Lesson Plan"
        verbose_name_plural = "Lesson Plans"

    def __str__(self):
        return self.goal


class QuestionBank(AbstractData):
    QUESTION_TYPE = (
        ('0', 'Oral Questions'),
        ('1', 'Name of the following '),
    )
    CATEGORY = (
        ('0', 'Intext'),
        ('1', 'Textbook Exercise'),
    )
    category = models.CharField('Category', max_length=50, choices=CATEGORY)
    question_type = models.CharField('Question Type', max_length=50, choices=QUESTION_TYPE)
    page_no = models.CharField('Page No', max_length=50)
    question_no = models.CharField('Question No', max_length=50)
    question = models.TextField('Question')
    answer = models.TextField('Answer')


    class Meta:
        verbose_name = "Question Bank"
        verbose_name_plural = "Question Banks"

    def __str__(self):
        return self.question


class WordSearch(AbstractData):
    image_field = models.FileField(upload_to='word_search')

    class Meta:
        verbose_name = "Word Search"
        verbose_name_plural = "Word Search"

    def image_tag(self):
        return format_html('<img href="{0}" src="{0}" width="100" height="100" />'.format(self.image_field.url))

    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.image_field.name


class BrainStorm(AbstractData):
    name = models.CharField('Name', max_length=50)
    brain_storm = models.TextField('Brain Storm')

    class Meta:
        verbose_name = "Brain Storm"
        verbose_name_plural = "Brain Storms"

    def __str__(self):
        return self.name


class TellYourTeacher(AbstractData):
    name = models.CharField('Name', max_length=50)
    tell_your_teacher = models.TextField('Tell your teacher')

    class Meta:
        verbose_name = "Tell Your Teacher"
        verbose_name_plural = "Tell Your Teachers"

    def __str__(self):
        return self.name


class FindOut(AbstractData):
    name = models.CharField('Name', max_length=50)
    find_out = models.TextField('Find Out')

    class Meta:
        verbose_name = "Find Out"
        verbose_name_plural = "Find Outs"

    def __str__(self):
        return self.name
