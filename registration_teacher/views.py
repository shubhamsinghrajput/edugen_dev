from django.shortcuts import render, redirect
from django.http import HttpResponse
from .teacher_model_form import *
from registration_school.views import send_otp
import http.client, json
from django.contrib.auth.models import User
from edugen import settings

key = settings.AUTH_KEY


def teacher(request):
    if request.session.get('cid'):
        request.session['cid'] == request.session.get('cid')
    else:
        request.session['cid'] = ''

    form = TeacherForm()
    if request.session.get('otp_message'):
        request.session['otp_message'] = request.session['otp_message']
    else:
        request.session['otp_message'] = ''

    if request.session.get('otp_message_error'):
        request.session['otp_message_error'] = request.session['otp_message_error']
    else:
        request.session['otp_message_error'] = ''

    if request.session.get('teacher_mess'):
        mess = request.session.get('teacher_mess')
    else:
        mess = ''

    if RegistrationSchool.objects.filter(cid=request.session['cid']).exists():
        request.session['school_id'] = RegistrationSchool.objects.get(cid=request.session['cid']).id
        object = RegistrationSchool.objects.get(cid=request.session['cid'])
    else:
        object = RegistrationSchool()

    context = {
        'object': object,
        'teacher_mess': mess,
        'otp_message': request.session['otp_message'],
        'otp_message_error': request.session['otp_message_error'],
        'classs': classes.objects.all(),
        'form': form,
    }
    return render(request, "teacher.html", context)


def teacher_update(request):
    request.session['teacher_cid_mess'] = ''
    request.session['teacher_mess'] = ''

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if RegistrationSchool.objects.filter(cid=request.POST['cid']).exists():
            request.session['teacher_mobile'] = str(request.POST['teacher_mobile_no'])
            request.session['school_mobile'] = str(
                RegistrationSchool.objects.get(cid=request.POST['cid']).school_mobile_no)

            if form.is_valid():
                form.save()
                request.session['teacher_mess'] = '''You got a otp on your mobile number.Please check and 
                                fill this otp fro verify your mobile number.......'''
            list_mobile_no = [request.session['teacher_mobile'], request.session['school_mobile']]
            for mobile_no in list_mobile_no:
                send_otp(request, mobile_no)

            return redirect('teacher')
        else:
            request.session['teacher_cid_mess'] = "Your CID is not match in our record."
            return render(request, "teacher.html", {'form': form, 'teacher_mess': request.session['teacher_mess'],
                                                    'teacher_cid_mess': request.session['teacher_cid_mess'], })

    else:
        context = {}
    return render(request, "teacher.html", context)


def confirm_email(request):
    try:
        token = request.GET.get('token')
    except:
        HttpResponse('Token is not match')

    data = RegistrationTeacher.objects.get(teacher_token=token)
    data.email_confirm = True
    data.save()
    return redirect('teacher')


def teacher_verify_otp(request):
    if not request.session.get('school_mobile') or not request.session.get(
            'teacher_mobile') or not request.session.get('school_otp') or not request.session.get('teacher_otp'):
        return HttpResponse('Mobile no is empty.')

    dict = {
        str(request.session['school_mobile']): str(request.POST['school_otp']),
        str(request.session['teacher_mobile']): str(request.POST['teacher_otp']),
    }

    conn = http.client.HTTPSConnection("control.msg91.com")

    payload = ""

    headers = {'content-type': "application/x-www-form-urlencoded"}
    otp_verified = {}
    otp_message = {}
    for mobile, otp in dict.items():
        conn.request("POST",
                     "/api/verifyRequestOTP.php?authkey=" + key + "&mobile=91" + mobile + "&otp=" + otp,
                     payload, headers)

        res = conn.getresponse()
        data = res.read().decode("utf-8")
        print(data)
        out = json.loads(data)
        # message = out["message"].replace("_", " ").capitalize()
        otp_verified[mobile] = out["type"]
        otp_message[mobile] = out["message"]
    if 'error' in otp_verified.values():
        request.session['otp_message_error'] = "OTP is not verified"
    else:
        record = RegistrationTeacher.objects.get(teacher_mobile_no=request.session['teacher_mobile'])
        record.mobile_confirm = True
        record.save()
        create_teacher_as_user(record)
        request.session['teacher_mess'] = 'We have sent a email for login our portal. Please check and login.'
        request.session['otp_message'] = 'OTP successfully verified'

    return redirect('teacher')


def create_teacher_as_user(data):
    if not User.objects.filter(username=data.teacher_email).exists():
        characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
        result = ''
        for i in range(0, 10):
            result += random.choice(characters)

        user = User()
        user.username = data.teacher_email
        user.email = data.teacher_email
        user.set_password(result)
        user.save()
        new_user_create_email(user, result)
    print("user created")
    return True


def new_user_create_email(user, password):
    subject = 'Account created'
    message = get_template('new_user_create_email.html').render(
        {
            # 'link': socket.gethostbyname(socket.gethostname()),
            'link': '127.0.0.1',
            'username': user.username,
            'password': password,
        }
    )

    send_mail(subject, message, user.email, [user.email], html_message=message,
              fail_silently=True)
    print("email  send")
    return True
