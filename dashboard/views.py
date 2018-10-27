from django.shortcuts import render, redirect
from registration_teacher.models import RegistrationTeacher
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    teacher_data = RegistrationTeacher.objects.filter(teacher_email=request.user.email)

    class_subject_data = {}
    for data in teacher_data:
        for row in data.classes.all():
            class_subject_data[row] = [data.teacher_subject.id]

    context = {
        'class_subject_records': class_subject_data,
    }

    return render(request, 'dashboard.html', context)


@login_required
def add_class_in_session(request):
    request.session['class_id'] = request.POST['class_id']
    request.session['subject_id'] = request.POST['subject_id']
    return redirect('/content/')
