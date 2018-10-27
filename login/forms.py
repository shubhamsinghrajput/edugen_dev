# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from prototype_site.lms.login.models import *
#
#
# class SignUpForm(UserCreationForm):
#     GENDER = (
#         ('', ''),
#         (1, 'Male'),
#         (2, 'Female'),
#         (3, 'Other'),
#     )
#     MARITAL_STATUS = (
#         ('', ''),
#         (1, 'Single'),
#         (2, 'Married'),
#         (3, 'Other'),
#     )
#     username = forms.CharField(
#         max_length=30,
#         min_length=5,
#         required=False,
#         help_text='5-10 characters. Letters, digits and @ . + - _ only.',
#         widget=forms.TextInput(attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Username'
#                                       }))
#     first_name = forms.CharField(
#         max_length=30,
#         required=False,
#         help_text='First name is required',
#         widget=forms.TextInput(attrs={'class': "input100", 'autocomplete': 'off', 'title': 'First name',
#                                       }))
#     password1 = forms.CharField(
#         label='Password',
#         max_length=16,
#         min_length=8,
#         required=False,
#         help_text="Your password must contain 8-16 characters. Letters, digits and @ . + -",
#         widget=forms.PasswordInput(attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Password',
#                                           }))
#     password2 = forms.CharField(
#         label='Confirm password',
#         max_length=16,
#         min_length=8,
#         required=False,
#         help_text='Confirm password is required',
#         widget=forms.PasswordInput(attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Confirm password',
#                                           }))
#     last_name = forms.CharField(
#         max_length=30,
#         required=False,
#         help_text='Last name is required',
#         widget=forms.TextInput(attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Last name',
#                                       }))
#     email = forms.EmailField(
#         max_length=254,
#         required=False,
#         help_text='Please enter a valid email address.',
#         widget=forms.TextInput(attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Email',
#                                       }))
#     gender = forms.CharField(
#         label='Gender',
#         required=False,
#         help_text='Gender is required',
#         widget=forms.Select(choices=GENDER, attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Gender',
#                                                    }))
#     status = forms.CharField(
#         label='Marital status',
#         required=False,
#         help_text='Marital status is required',
#         widget=forms.Select(choices=MARITAL_STATUS,
#                             attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Marital status',
#                                    }))
#     education = forms.ModelChoiceField(
#         label='Highest educational degree',
#         empty_label='',
#         required=False,
#         help_text='Highest educational degree is required',
#         queryset=Education.objects.all(),
#         widget=forms.Select(
#             attrs={'class': "input100", 'autocomplete': 'off',
#                    'title': 'Highest educational degree',
#                    }))
#     primary_education = forms.ModelChoiceField(
#         label='Primary educational field',
#         required=False,
#         empty_label='',
#         help_text='Primary educational is required',
#         queryset=PrimaryEducation.objects.all(),
#         widget=forms.Select(
#             attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Primary educational field',
#                    }))
#     occupation = forms.ModelChoiceField(
#         label='Current occupation',
#         required=False,
#         empty_label='',
#         help_text='Current occupation is required',
#         queryset=Occupation.objects.all(),
#         widget=forms.Select(
#             attrs={'class': "input100", 'autocomplete': 'off',
#                    'title': 'Current occupation',
#                    }))
#     industry = forms.ModelChoiceField(
#         label='Industry',
#         required=False,
#         empty_label='',
#         help_text='Industry is required',
#         queryset=Industry.objects.all(),
#         widget=forms.Select(
#             attrs={'class': "input100", 'autocomplete': 'off', 'title': 'Industry',
#                    }))
#     primary_learning_objective = forms.CharField(
#         label='Primary learning objectives',
#         required=False,
#         help_text='(Which skills do you want to learn ?)',
#         widget=forms.TextInput(
#             attrs={'class': "input100", 'autocomplete': 'off',
#                    'title': 'Primary learning objectives',
#                    }))
#     country = forms.CharField(
#         label='Nationality',
#         required=False,
#         help_text='Nationality is required',
#         widget=forms.Select(choices=countries,
#                             attrs={'class': "input100", 'autocomplete': 'off',
#                                    'title': 'Nationality',
#                                    }))
#     date_of_birth = forms.DateField(
#         required=False,
#         help_text='(Date of birth format is dd-mm-yyyy)',
#         widget=forms.TextInput(
#             attrs={'class': "input100", 'autocomplete': 'off',
#                    'title': 'Date of birth format is yyyy-mm-dd',
#                    }))
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'password1',
#             'password2',
#             'first_name',
#             'last_name',
#             'email',
#             'gender',
#             'status',
#             'education',
#             'primary_education',
#             'occupation',
#             'industry',
#             'primary_learning_objective',
#             'date_of_birth',
#             'country')
