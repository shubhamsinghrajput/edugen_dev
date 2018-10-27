from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import http.client, json
from edugen import settings
from random import randint

key = settings.AUTH_KEY


def index(request):
    if request.GET.get('cid'):
        request.session['school_mess'] = ''
        request.session['cid'] = request.GET.get('cid')
    elif request.session.get('cid'):
        request.session['cid'] == request.session.get('cid')
    else:
        request.session['cid'] = ''

    if request.session.get('school_mess'):
        school_mess = request.session.get('school_mess')
    else:
        school_mess = ''

    if RegistrationSchool.objects.filter(cid=request.session['cid']).exists():
        request.session['school_id'] = RegistrationSchool.objects.get(cid=request.session['cid']).id
        object = RegistrationSchool.objects.get(cid=request.session['cid'])
    else:
        object = RegistrationSchool()

    context = {
        'object': object,
        'school_mess': school_mess,
        'cid': request.session['cid'],
    }
    return render(request, "school.html", context)


def update(request):
    request.session['cid'] = request.session['cid']
    if request.method == 'POST':
        if request.session['cid']:
            object = RegistrationSchool()
            object.id = request.session['school_id']
            object.cid = request.session['cid']
            object.school_name = request.POST['school_name']
            object.school_email = request.POST['school_email']
            object.school_mobile_no = request.POST['school_mobile_no']
            object.school_address = request.POST['school_address']
            object.user_type = request.POST['user_type']
            object.save()
            send_otp(request, mobile_no=request.POST['school_mobile_no'])
            request.session['school_mess'] = '''You got a otp on your mobile number.Please check and 
                                fill this otp fro verify your mobile number.'''

            return redirect('index')
        else:
            context = {
                'school_mess_error': "Your CID is empty.",
            }

    else:
        context = {}
    return render(request, "school.html", context)


def send_otp(request, mobile_no):
    if not mobile_no:
        return HttpResponse('Mobile no is empty.')

    conn = http.client.HTTPConnection("control.msg91.com")
    payload = ""
    otp = str(generateOtp(request))
    conn.request("POST",
                 "/api/sendotp.php?"
                 "authkey=" + key + "&"
                                    "message= Your verification code is " + otp + "&"
                                                                                  "sender=Edugen"
                                                                                  "&mobile=91" + mobile_no +
                 "&otp=" + otp, payload)
    res = conn.getresponse()
    data = res.read()
    return redirect('index')


def verify_otp(request):
    if not request.session.get('cid'):
        return HttpResponse('Mobile no is empty.')
    mobile_no = str(RegistrationSchool.objects.get(cid=request.session['cid']).school_mobile_no)
    otp = str(request.POST['otp'])
    conn = http.client.HTTPSConnection("control.msg91.com")

    payload = ""

    headers = {'content-type': "application/x-www-form-urlencoded"}

    conn.request("POST",
                 "/api/verifyRequestOTP.php?authkey=" + key + "&mobile=91" + mobile_no + "&otp=" + otp,
                 payload, headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    out = json.loads(data)
    message = out["message"].replace("_", " ").capitalize()

    if out["type"] == 'success':
        record = RegistrationSchool.objects.get(cid=request.session['cid'])
        record.mobile_confirm = True
        record.save()
        context = {
            'otp_message': message,
            'object': RegistrationSchool.objects.get(cid=request.session['cid']),
            'cid': request.session['cid'],
        }
    else:
        context = {
            'otp_message_error': message,
            'object': RegistrationSchool.objects.get(cid=request.session['cid']),
            'cid': request.session['cid'],
        }
    return render(request, "school.html", context)


def resend_otp(request):
    conn = http.client.HTTPConnection("control.msg91.com")

    payload = ""

    headers = {'content-type': "application/x-www-form-urlencoded"}

    conn.request("POST", "/api/retryotp.php?authkey=" + key + "&mobile=919870746097&retrytype=text", payload,
                 headers)

    res = conn.getresponse()
    data = res.read()
    return HttpResponse(data.decode("utf-8"))


def generateOtp(request):
    return randint(1000, 9999)
