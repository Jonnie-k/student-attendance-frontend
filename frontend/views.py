import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

BASE_API = "http://127.0.0.1:8000/api"


@login_required
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


# ==========================
# STUDENTS
# ==========================

@login_required
def students(request):
    search = request.GET.get("search", "")

    response = requests.get(f"{BASE_API}/students/")
    students = response.json()
    print("STATUS:", response.status_code)
    print("DATA:" , students)

    if isinstance(students, dict):
        students = students.get("results", students)

    if search:
        search = search.lower()

        students = [
            student for student in students
            if (
                search in student.get("username", "").lower()
                or search in student.get("full_name", "").lower()
                or search in student.get("admission_number", "").lower()
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


@login_required
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
            json=data,
        )

        if response.status_code == 201:
            messages.success(request, "Student added successfully.")
            return redirect("students")

        return render(
            request,
            "frontend/student_form.html",
            {
                "error": response.json(),
            },
        )

    return render(request, "frontend/student_form.html")


@login_required
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
            messages.success(request, "Student updated successfully.")
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

    messages.error(request, "Student not found.")
    return redirect("students")


@login_required
def delete_student(request, student_id):
    url = f"{BASE_API}/students/{student_id}/"

    if request.method == "POST":
        requests.delete(url)
        messages.success(request, "Student deleted successfully.")
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

    messages.error(request, "Student not found.")
    return redirect("students")


# ==========================
# TEACHERS
# ==========================

@login_required
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
                search in teacher.get("username", "").lower()
                or search in teacher.get("full_name", "").lower()
                or search in teacher.get("employee_number", "").lower()
                or search in teacher.get("department", "").lower()
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


@login_required
def add_teacher(request):
    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "employee_number": request.POST.get("employee_number"),
            "department": request.POST.get("department"),
        }
        response = requests.post(
            f"{BASE_API}/teachers/",
            json=data,
        )

        if response.status_code == 201:
            messages.success(request, "Teacher added successfully.")
            return redirect("teachers")

        return render(
            request,
            "frontend/teacher_form.html",
            {
                "error": response.json(),
            },
        )

    return render(request, "frontend/teacher_form.html")


@login_required
def edit_teacher(request, teacher_id):
    url = f"{BASE_API}/teachers/{teacher_id}/"

    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "employee_number": request.POST.get("employee_number"),
            "department": request.POST.get("department"),
        }
        response = requests.put(url, json=data)

        if response.status_code == 200:
            messages.success(request, "Teacher updated successfully.")
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

    messages.error(request, "Teacher not found.")
    return redirect("teachers")


@login_required
def delete_teacher(request, teacher_id):
    url = f"{BASE_API}/teachers/{teacher_id}/"

    if request.method == "POST":
        requests.delete(url)
        messages.success(request, "Teacher deleted successfully.")
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

    messages.error(request, "Teacher not found.")
    return redirect("teachers")


# ==========================
# COURSES
# ==========================

@login_required
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
            if (
                search in course.get("course_name", "").lower()
                or search in course.get("course_code", "").lower()
                or search in course.get("teacher_name", "").lower()
            )
        ]
    return render(
        request,
        "frontend/courses.html",
        {
            "courses": courses,
            "search": search,
        },
    )


@login_required
def add_course(request):
    teachers = requests.get(f"{BASE_API}/teachers/").json()

    if isinstance(teachers, dict):
        teachers = teachers.get("results", teachers)

    if request.method == "POST":
        data = {
            "course_name": request.POST.get("course_name"),
            "course_code": request.POST.get("course_code"),
            "teacher": request.POST.get("teacher"),
        }

        response = requests.post(
            f"{BASE_API}/courses/",
            json=data,
        )

        if response.status_code == 201:
            messages.success(request, "Course added successfully.")
            return redirect("courses")

        return render(
            request,
            "frontend/course_form.html",
            {
                "teachers": teachers,
                "error": response.json(),
            },
        )

    return render(
        request,
        "frontend/course_form.html",
        {
            "teachers": teachers,
        },
    )


@login_required
def edit_course(request, course_id):
    teachers = requests.get(f"{BASE_API}/teachers/").json()

    if isinstance(teachers, dict):
        teachers = teachers.get("results", teachers)

    url = f"{BASE_API}/courses/{course_id}/"

    if request.method == "POST":
        data = {
            "course_name": request.POST.get("course_name"),
            "course_code": request.POST.get("course_code"),
            "teacher": request.POST.get("teacher"),
        }

        response = requests.put(url, json=data)

        if response.status_code == 200:
            messages.success(request, "Course updated successfully.")
            return redirect("courses")

        return render(
            request,
            "frontend/course_form.html",
            {
                "teachers": teachers,
                "course": data,
                "error": response.json(),
            },
        )

    response = requests.get(url)

    if response.status_code == 200:
        course = response.json()

        return render(
            request,
            "frontend/course_form.html",
            {
                "teachers": teachers,
                "course": course,
            },
        )

    messages.error(request, "Course not found.")
    return redirect("courses")


@login_required
def delete_course(request, course_id):
    url = f"{BASE_API}/courses/{course_id}/"

    if request.method == "POST":
        requests.delete(url)
        messages.success(request, "Course deleted successfully.")
        return redirect("courses")

    response = requests.get(url)

    if response.status_code == 200:
        course = response.json()

        return render(
            request,
            "frontend/course_delete.html",
            {
                "course": course,
            },
        )

    messages.error(request, "Course not found.")
    return redirect("courses")


# ==========================
# ATTENDANCE
# ==========================

@login_required
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
            if (
                search in record.get("student_name", "").lower()
                or search in record.get("course_name", "").lower()
                or search in record.get("status", "").lower()
                or search in record.get("date", "").lower()
            )
        ]

    return render(
        request,
        "frontend/attendance.html",
        {
            "attendance": attendance,
            "search": search,
        },
    )


@login_required
def add_attendance(request):
    students = requests.get(f"{BASE_API}/students/").json()
    courses = requests.get(f"{BASE_API}/courses/").json()

    if isinstance(students, dict):
        students = students.get("results", students)

    if isinstance(courses, dict):
        courses = courses.get("results", courses)

    if request.method == "POST":
        data = {
            "student": request.POST.get("student"),
            "course": request.POST.get("course"),
            "date": request.POST.get("date"),
            "status": request.POST.get("status"),
        }

        response = requests.post(
            f"{BASE_API}/attendance/",
            json=data,
        )

        if response.status_code == 201:
            messages.success(request, "Attendance record added successfully.")
            return redirect("attendance")

        return render(
            request,
            "frontend/attendance_form.html",
            {
                "students": students,
                "courses": courses,
                "error": response.json(),
            },
        )

    return render(
        request,
        "frontend/attendance_form.html",
        {
            "students": students,
            "courses": courses,
        },
    )


@login_required
def edit_attendance(request, attendance_id):
    students = requests.get(f"{BASE_API}/students/").json()
    courses = requests.get(f"{BASE_API}/courses/").json()

    if isinstance(students, dict):
        students = students.get("results", students)

    if isinstance(courses, dict):
        courses = courses.get("results", courses)

    url = f"{BASE_API}/attendance/{attendance_id}/"

    if request.method == "POST":
        data = {
            "student": request.POST.get("student"),
            "course": request.POST.get("course"),
            "date": request.POST.get("date"),
            "status": request.POST.get("status"),
        }

        response = requests.put(url, json=data)

        if response.status_code == 200:
            messages.success(request, "Attendance record updated successfully.")
            return redirect("attendance")

        return render(
            request,
            "frontend/attendance_form.html",
            {
                "attendance": data,
                "students": students,
                "courses": courses,
                "error": response.json(),
            },
        )

    response = requests.get(url)

    if response.status_code == 200:
        attendance = response.json()

        return render(
            request,
            "frontend/attendance_form.html",
            {
                "attendance": attendance,
                "students": students,
                "courses": courses,
            },
        )

    messages.error(request, "Attendance record not found.")
    return redirect("attendance")


@login_required
def delete_attendance(request, attendance_id):
    url = f"{BASE_API}/attendance/{attendance_id}/"

    if request.method == "POST":
        requests.delete(url)
        messages.success(request, "Attendance record deleted successfully.")
        return redirect("attendance")

    response = requests.get(url)

    if response.status_code == 200:
        attendance = response.json()

        return render(
            request,
            "frontend/attendance_delete.html",
            {
                "attendance": attendance,
            },
        )

    messages.error(request, "Attendance record not found.")
    return redirect("attendance")


@login_required
def reports(request):
    response = requests.get(f"{BASE_API}/attendance/")
    attendance = response.json()

    if isinstance(attendance, dict):
        attendance = attendance.get("results", attendance)

    # Get filter values
    student = request.GET.get("student", "")
    course = request.GET.get("course", "")
    status = request.GET.get("status", "")
    date = request.GET.get("date", "")

    # Apply filters
    if student:
        attendance = [
            record for record in attendance
            if student.lower() in record.get("student_name", "").lower()
        ]

    if course:
        attendance = [
            record for record in attendance
            if course.lower() in record.get("course_name", "").lower()
        ]

    if status:
        attendance = [
            record for record in attendance
            if record.get("status") == status
        ]

    if date:
        attendance = [
            record for record in attendance
            if record.get("date") == date
        ]

    total_records = len(attendance)

    present_count = sum(
        1 for record in attendance
        if record.get("status") == "Present"
    )

    absent_count = sum(
        1 for record in attendance
        if record.get("status") == "Absent"
    )

    late_count = sum(
        1 for record in attendance
        if record.get("status") == "Late"
    )

    attendance_percentage = (
        (present_count / total_records) * 100
        if total_records else 0
    )

    context = {
        "attendance": attendance,
        "total_records": total_records,
        "present_count": present_count,
        "absent_count": absent_count,
        "late_count": late_count,
        "attendance_percentage": round(attendance_percentage, 1),

        "student": student,
        "course": course,
        "status": status,
        "date": date,
    }

    return render(
        request,
        "frontend/reports.html",
        context,
    )