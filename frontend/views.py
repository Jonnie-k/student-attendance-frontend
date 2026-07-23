import requests
from django.shortcuts import render

API_URL = "http://127.0.0.1:8000/api/students/"


def students(request):
    response = requests.get(API_URL)

    if response.status_code == 200:
        students = response.json()
    else:
        students = []

    return render(
        request,
        "frontend/students.html",
        {"students": students},
    )