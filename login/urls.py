from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("login/", auth_views.login, {'template_name': 'login.html'}, name='login'),
    path("logout/", auth_views.logout, {'next_page': 'login'}, name='logout'),
    # # path("signup", views.signup, name='signup'),
    # path('password_reset/', auth_views.password_reset, {'template_name': 'password_reset_form.html'},
    #      name='password_reset'),
    # path('password_reset/done/', auth_views.password_reset_done, {'template_name': 'password_reset_done.html'},
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.password_reset_confirm, {'template_name': 'password_reset_confirm.html'},
    #      name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, {'template_name': 'password_reset_complete.html'},
    #      name='password_reset_complete'),
]
