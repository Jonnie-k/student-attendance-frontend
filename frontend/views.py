import requests
from django.shortcuts import render

BASE_API = "http://127.0.0.1:8000/api"


def home(request):
    students = requests.get(f"{BASE_API}/students/").json()
    teachers = requests.get(f"{BASE_API}/teachers/").json()
    courses = requests.get(f"{BASE_API}/courses/").json()
    attendance = requests.get(f"{BASE_API}/attendance/").json()

    if isinstance(students, dict):
        students = students.get("results", students)

    if isinstance(teachers, dict):
        teachers = teachers.get("results", teachers)

    if isinstance(courses, dict):
        courses = courses.get("results", courses)

    if isinstance(attendance, dict):
        attendance = attendance.get("results", attendance)

    context = {
        "student_count": len(students),
        "teacher_count": len(teachers),
        "course_count": len(courses),
        "attendance_count": len(attendance),
    }

    return render(request, "frontend/home.html", context)

def students(request):
    search = request.GET.get("search", "")

    response = requests.get(f"{BASE_API}/students/")
    students = response.json()

    if isinstance(students, dict):
        students = students.get("results", students)

    if search:
        search = search.lower()
        students = [
            student for student in students
         if (
    search in student["username"].lower()
    or search in student["full_name"].lower()
    or search in student["admission_number"].lower()
)
        ]

    return render(
        request,
        "frontend/students.html",
        {
            "students": students,
            "search": search,
        },
    )

def teachers(request):
    search = request.GET.get("search", "")

    response = requests.get(f"{BASE_API}/teachers/")
    teachers = response.json()

    if isinstance(teachers, dict):
        teachers = teachers.get("results", teachers)

    if search:
        search = search.lower()
        teachers = [
            teacher for teacher in teachers
          if (
    search in teacher["username"].lower()
    or search in teacher["full_name"].lower()
    or search in teacher["employee_number"].lower()
    or search in teacher["department"].lower()
)
        ]

    return render(
        request,
        "frontend/teachers.html",
        {
            "teachers": teachers,
            "search": search,
        },
    )
def courses(request):
    search = request.GET.get("search", "")

    response = requests.get(f"{BASE_API}/courses/")
    courses = response.json()

    if isinstance(courses, dict):
        courses = courses.get("results", courses)

    if search:
        search = search.lower()
        courses = [
            course for course in courses
            if search in course["course_name"].lower()
            or search in course["course_code"].lower()
        ]

    return render(
        request,
        "frontend/courses.html",
        {
            "courses": courses,
            "search": search,
        },
    )
def attendance(request):
    search = request.GET.get("search", "")

    response = requests.get(f"{BASE_API}/attendance/")
    attendance = response.json()

    if isinstance(attendance, dict):
        attendance = attendance.get("results", attendance)

    if search:
        search = search.lower()
        attendance = [
            record for record in attendance
            if search in record["student"]["user"]["username"].lower()
            or search in record["course"]["course_name"].lower()
        ]

    return render(
        request,
        "frontend/attendance.html",
        {
            "attendance": attendance,
            "search": search,
        },
    )