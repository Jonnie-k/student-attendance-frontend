from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.students, name="students"),
    path("students/add/", views.add_student, name="add_student"),
    path("teachers/", views.teachers, name="teachers"),
    path("courses/", views.courses, name="courses"),
    path("attendance/", views.attendance, name="attendance"),
]