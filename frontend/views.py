import requests
from django.shortcuts import render

BASE_API = "http://127.0.0.1:8000/api"


def home(request):
    return render(request, "frontend/home.html")


def students(request):
    response = requests.get(f"{BASE_API}/students/")
    data = response.json()
    return render(request, "frontend/students.html", {"students": data})


def teachers(request):
    response = requests.get(f"{BASE_API}/teachers/")
    data = response.json()
    return render(request, "frontend/teachers.html", {"teachers": data})


def courses(request):
    response = requests.get(f"{BASE_API}/courses/")
    data = response.json()
    return render(request, "frontend/courses.html", {"courses": data})


def attendance(request):
    response = requests.get(f"{BASE_API}/attendance/")
    data = response.json()
    return render(request, "frontend/attendance.html", {"attendance": data})