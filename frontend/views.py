import requests
from django.shortcuts import render, redirect

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
def add_student(request):
    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "admission_number": request.POST.get("admission_number"),
            "phone_number": request.POST.get("phone_number"),
            "gender": request.POST.get("gender"),
        }

        response = requests.post(
            f"{BASE_API}/students/",
            json=data
        )

        if response.status_code == 201:
            return redirect("students")

        return render(
            request,
            "frontend/student_form.html",
            {
                "error": response.json()
            },
        )

    return render(
        request,
        "frontend/student_form.html",
    )
def edit_student(request, student_id):
    url = f"{BASE_API}/students/{student_id}/"

    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "admission_number": request.POST.get("admission_number"),
            "phone_number": request.POST.get("phone_number"),
            "gender": request.POST.get("gender"),
        }

        response = requests.put(url, json=data)

        if response.status_code == 200:
            return redirect("students")

        return render(
            request,
            "frontend/student_form.html",
            {
                "student": data,
                "error": response.json(),
            },
        )

    response = requests.get(url)

    if response.status_code == 200:
        student = response.json()

        return render(
            request,
            "frontend/student_form.html",
            {
                "student": student,
            },
        )

    return redirect("students")
def delete_student(request, student_id):
    url = f"{BASE_API}/students/{student_id}/"

    if request.method == "POST":
        response = requests.delete(url)

        if response.status_code == 204:
            return redirect("students")

        return redirect("students")

    response = requests.get(url)

    if response.status_code == 200:
        student = response.json()

        return render(
            request,
            "frontend/student_delete.html",
            {
                "student": student,
            },
        )

    return redirect("students")

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
def add_teacher(request):
    if request.method == "POST":
        data = {
            "user": request.POST.get("user"),
            "employee_number": request.POST.get("employee_number"),
            "department": request.POST.get("department"),
        }

        response = requests.post(f"{BASE_API}/teachers/", json=data)

        if response.status_code == 201:
            return redirect("teachers")

        return render(
            request,
            "frontend/teacher_form.html",
            {"error": response.json()},
        )

    return render(request, "frontend/teacher_form.html")
def edit_teacher(request, teacher_id):
    url = f"{BASE_API}/teachers/{teacher_id}/"

    if request.method == "POST":
        data = {
            "user": request.POST.get("user"),
            "employee_number": request.POST.get("employee_number"),
            "department": request.POST.get("department"),
        }

        response = requests.put(url, json=data)

        if response.status_code == 200:
            return redirect("teachers")

        return render(
            request,
            "frontend/teacher_form.html",
            {
                "teacher": data,
                "error": response.json(),
            },
        )

    response = requests.get(url)

    if response.status_code == 200:
        teacher = response.json()

        return render(
            request,
            "frontend/teacher_form.html",
            {
                "teacher": teacher,
            },
        )

    return redirect("teachers")

def delete_teacher(request, teacher_id):
    url = f"{BASE_API}/teachers/{teacher_id}/"

    if request.method == "POST":
        requests.delete(url)
        return redirect("teachers")

    response = requests.get(url)

    if response.status_code == 200:
        teacher = response.json()

        return render(
            request,
            "frontend/teacher_delete.html",
            {
                "teacher": teacher,
            },
        )

    return redirect("teachers")

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