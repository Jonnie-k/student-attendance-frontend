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
    teachers = response.json()

    if isinstance(teachers, dict) and "results" in teachers:
        teachers = teachers["results"]

    return render(
        request,
        "frontend/teachers.html",
        {"teachers": teachers},
    )
def courses(request):
    response = requests.get(f"{BASE_API}/courses/")
    courses = response.json()

    if isinstance(courses, dict) and "results" in courses:
        courses = courses["results"]

    return render(
        request,
        "frontend/courses.html",
        {"courses": courses},
    )

def attendance(request):
    response = requests.get(f"{BASE_API}/attendance/")
    attendance_records = response.json()

    if isinstance(attendance_records, dict) and "results" in attendance_records:
        attendance_records = attendance_records["results"]

    return render(
        request,
        "frontend/attendance.html",
        {"attendance_records": attendance_records},
    )