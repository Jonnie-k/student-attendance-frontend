from django.contrib import admin
from django.contrib.admindocs import views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("frontend.urls")),
    path("students/add/", views.add_student, name="add_student"),
]