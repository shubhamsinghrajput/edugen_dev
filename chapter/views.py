from django.shortcuts import render, redirect
from chapter.models import *
from django.contrib.auth.decorators import login_required
import collections


@login_required
def content(request):
    class_with_unit_data = UnitWithChapters.objects.filter(class_name=request.session['class_id'],
                                                           subject=request.session['subject_id'])

    chapter_data = collections.defaultdict(dict)

    for data in class_with_unit_data:
        key1 = data.unit_name
        key2 = data.chapter_no
        chapter_data[key1][key2] = data.chapter_name

    context = {
        'class_with_unit_dict': chapter_data.items(),
    }
    return render(request, 'content.html', context)


@login_required
def add_chapter_in_session(request):
    request.session['chapter_no'] = request.POST['chapter_no']
    return redirect('/lesson/')


@login_required
def add_question_type_in_session(request):
    data = request.POST['id']
    category, type = data.split('_')
    request.session['category'] = category
    request.session['type'] = type
    return redirect('/question/')


@login_required
def lesson(request):
    lesson_plan_data = LessonPlan()

    if LessonPlan.objects.filter(class_name=request.session['class_id'],
                                 subject=request.session['subject_id'],
                                 chapter_no=request.session['chapter_no']).exists():
        lesson_plan_data = LessonPlan.objects.get(class_name=request.session['class_id'],
                                                  subject=request.session['subject_id'],
                                                  chapter_no=request.session['chapter_no'])
    unit_with_chapter = UnitWithChapters.objects.get(class_name=request.session['class_id'],
                                                     subject=request.session['subject_id'],
                                                     chapter_no=request.session['chapter_no'])

    context = {
        'lesson_plan_data': lesson_plan_data,
        'unit_with_chapter': unit_with_chapter,
    }
    return render(request, 'lesson.html', context)


@login_required
def question_bank(request):
    unit_with_chapter = UnitWithChapters.objects.get(class_name=request.session['class_id'],
                                                     subject=request.session['subject_id'],
                                                     chapter_no=request.session['chapter_no'])
    context = {
        'unit_with_chapter': unit_with_chapter,
    }
    return render(request, 'question_form.html', context)


@login_required
def question(request):
    question_bank_records = {}
    if request.session['category'] == '0':
        string_value = "Intext"
    else:
        string_value = "Textbook Exercise"
    if request.session['type'] == '0':
        type_value = "Oral Questions"
    else:
        type_value = "Name of the following "

    if QuestionBank.objects.filter(class_name=request.session['class_id'],
                                   subject=request.session['subject_id'],
                                   chapter_no=request.session['chapter_no'],
                                   category=request.session['category'],
                                   question_type=request.session['type']).exists():
        question_bank_records = QuestionBank.objects.filter(class_name=request.session['class_id'],
                                                            subject=request.session['subject_id'],
                                                            chapter_no=request.session['chapter_no'],
                                                            category=request.session['category'],
                                                            question_type=request.session['type'])
    unit_with_chapter = UnitWithChapters.objects.get(class_name=request.session['class_id'],
                                                     subject=request.session['subject_id'],
                                                     chapter_no=request.session['chapter_no'])

    context = {
        'question_bank_records': question_bank_records,
        'unit_with_chapter': unit_with_chapter,
        'question_type_bar_string': string_value,
        'type_value': type_value,

    }
    return render(request, 'question.html', context)


@login_required
def word_search(request):
    word_search_record = {}

    if WordSearch.objects.filter(class_name=request.session['class_id'],
                                 subject=request.session['subject_id'],
                                 chapter_no=request.session['chapter_no']).exists():
        word_search_record = WordSearch.objects.get(class_name=request.session['class_id'],
                                                    subject=request.session['subject_id'],
                                                    chapter_no=request.session['chapter_no'])
    unit_with_chapter = UnitWithChapters.objects.get(class_name=request.session['class_id'],
                                                     subject=request.session['subject_id'],
                                                     chapter_no=request.session['chapter_no'])

    context = {
        'word_search_record': word_search_record,
        'unit_with_chapter': unit_with_chapter,
    }
    return render(request, 'word_search.html', context)


@login_required
def brain_storm(request):
    brain_storm_data = BrainStorm()

    if BrainStorm.objects.filter(class_name=request.session['class_id'],
                                 subject=request.session['subject_id'],
                                 chapter_no=request.session['chapter_no']).exists():
        brain_storm_data = BrainStorm.objects.get(class_name=request.session['class_id'],
                                                  subject=request.session['subject_id'],
                                                  chapter_no=request.session['chapter_no'])
    unit_with_chapter = UnitWithChapters.objects.get(class_name=request.session['class_id'],
                                                     subject=request.session['subject_id'],
                                                     chapter_no=request.session['chapter_no'])

    context = {
        'brain_storm_data': brain_storm_data,
        'unit_with_chapter': unit_with_chapter,
    }
    return render(request, 'brain_storm.html', context)


@login_required
def tell_your_teacher(request):
    tell_your_teacher_data = TellYourTeacher()

    if TellYourTeacher.objects.filter(class_name=request.session['class_id'],
                                      subject=request.session['subject_id'],
                                      chapter_no=request.session['chapter_no']).exists():
        tell_your_teacher_data = TellYourTeacher.objects.get(class_name=request.session['class_id'],
                                                             subject=request.session['subject_id'],
                                                             chapter_no=request.session['chapter_no'])
    unit_with_chapter = UnitWithChapters.objects.get(class_name=request.session['class_id'],
                                                     subject=request.session['subject_id'],
                                                     chapter_no=request.session['chapter_no'])

    context = {
        'tell_your_teacher_data': tell_your_teacher_data,
        'unit_with_chapter': unit_with_chapter,
    }
    return render(request, 'tell_your_teacher.html', context)


@login_required
def find_out(request):
    find_out_data = FindOut()

    if FindOut.objects.filter(class_name=request.session['class_id'],
                              subject=request.session['subject_id'],
                              chapter_no=request.session['chapter_no']).exists():
        find_out_data = FindOut.objects.get(class_name=request.session['class_id'],
                                            subject=request.session['subject_id'],
                                            chapter_no=request.session['chapter_no'])
    unit_with_chapter = UnitWithChapters.objects.get(class_name=request.session['class_id'],
                                                     subject=request.session['subject_id'],
                                                     chapter_no=request.session['chapter_no'])

    context = {
        'find_out_data': find_out_data,
        'unit_with_chapter': unit_with_chapter,
    }
    return render(request, 'find_out.html', context)
