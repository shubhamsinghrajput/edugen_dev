from django.urls import path
from dashboard import views

urlpatterns = [
    path("dashboard/", views.dashboard, name='dashboard'),
    path("add_class_in_session/", views.add_class_in_session, name='add_class_in_session'),
]
