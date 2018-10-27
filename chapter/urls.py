from django.urls import path
from chapter import views

urlpatterns = [
    path("content/", views.content, name='content'),
    path("add_chapter_in_session/", views.add_chapter_in_session, name='add_chapter_in_session'),
    path("lesson/", views.lesson, name='lesson'),
    path("question_bank/", views.question_bank, name='question_bank'),
    path("add_question_type_in_session/", views.add_question_type_in_session, name='add_question_type_in_session'),
    path("question/", views.question, name='question'),
    path("word_search/", views.word_search, name='word_search'),
    path("brain_storm/", views.brain_storm, name='brain_storm'),
    path("tell_your_teacher/", views.tell_your_teacher, name='tell_your_teacher'),
    path("find_out/", views.find_out, name='find_out'),
]
