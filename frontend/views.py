import requests
from django.shortcuts import render

BASE_API = "http://127.0.0.1:8000/api"


def home(request):
    return render(request, "frontend/home.html")


def students(request):
    response = requests.get(f"{BASE_API}/students/")

    if response.status_code == 200:
        students = response.json()
    else:
        students = []

    return render(
        request,
        "frontend/students.html",
        {"students": students},
    )