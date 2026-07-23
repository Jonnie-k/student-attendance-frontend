from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
   path("students/", views.students, name="students"),
path("students/add/", views.add_student, name="add_student"),
path(
    "students/edit/<int:student_id>/",
    views.edit_student,
    name="edit_student",
),
]