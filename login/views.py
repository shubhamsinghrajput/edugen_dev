# from .models import *
# from django.contrib.auth import login, authenticate
# from edugen.login.forms import SignUpForm
# from django.shortcuts import render, redirect
#
#
# def signup(request):
#     icons = ['fa fa-user', 'fa fa-lock', 'fa fa-lock', 'fa fa-user', 'fa fa-user', 'fa fa-envelope',
#              'fa fa-venus-mars', 'fa fa-slideshare',
#              'fa fa-graduation-cap', 'fa fa-briefcase', 'fa fa-university', 'fa fa-industry', 'fa fa-list-ol',
#              'fa fa-calendar',
#              'fa fa-globe']
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             gender = request.POST['gender']
#             status = request.POST['status']
#             education = request.POST['education']
#             primary_education = request.POST['primary_education']
#             occupation = request.POST['occupation']
#             industry = request.POST['industry']
#             primary_learning_objective = request.POST['primary_learning_objective']
#             country = request.POST['country']
#             date_of_birth = request.POST['date_of_birth']
#
#             Profile.objects.create(gender=gender, status=status, education_id=education,
#                                    primary_education_id=primary_education,
#                                    occupation_id=occupation,
#                                    industry_id=industry, primary_learning_objective=primary_learning_objective,
#                                    country=country, date_of_birth=date_of_birth, user_id=user.id)
#
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form, 'icons': icons})
