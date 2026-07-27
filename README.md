# Student Attendance System — Frontend

A Django web application that serves as the user interface for the Student Attendance Management System. It communicates with the [backend REST API](https://student-attendance-backend-h3hr.onrender.com/api) to manage students, teachers, courses, attendance records, and generate reports.

**Live Demo:** https://student-attendance-frontend-mupu.onrender.com

---

## Features

- **Dashboard** — Overview of total students, teachers, courses, and attendance records
- **Students** — Add, edit, delete, and search students
- **Teachers** — Add, edit, delete, and search teachers
- **Courses** — Add, edit, delete, and search courses with teacher assignment
- **Attendance** — Record, edit, delete, and search attendance per student per course
- **Reports** — Filter attendance by student, course, date, and status with summary statistics
- **Authentication** — Login/logout with session-based auth and protected routes

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6.0.7 |
| Templating | Django Templates |
| Styling | Bootstrap 5.3 + Bootstrap Icons |
| Static Files | WhiteNoise |
| API Communication | Python `requests` library |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Deployment | Render (Gunicorn + WhiteNoise) |

---

## Project Structure

```
student-attendance-frontend/
├── frontend/
│   ├── auth_views.py       # Custom login/logout views
│   ├── views.py            # All page views (students, teachers, courses, attendance, reports)
│   └── urls.py             # URL routing
├── frontend_project/
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL config
│   └── wsgi.py
├── templates/
│   ├── frontend/           # All HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── students.html
│   │   ├── student_form.html
│   │   ├── student_delete.html
│   │   ├── teachers.html
│   │   ├── teacher_form.html
│   │   ├── teacher_delete.html
│   │   ├── courses.html
│   │   ├── course_form.html
│   │   ├── course_delete.html
│   │   ├── attendance.html
│   │   ├── attendance_form.html
│   │   ├── attendance_delete.html
│   │   └── reports.html
│   └── registration/
│       └── login.html
├── static/
│   └── css/
│       └── style.css
├── .env                    # Local environment variables (not committed)
├── .gitignore
├── manage.py
├── requirements.txt
└── Procfile
```

---

## Local Setup

### Prerequisites

- Python 3.12+
- The backend API running (see [backend repo](../student-attendance-backend/))

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Student-Attendance-System.git
cd Student-Attendance-System

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r student-attendance-frontend/requirements.txt

# 4. Create the .env file
cd student-attendance-frontend
cp .env.example .env   # or create manually (see below)

# 5. Collect static files
python manage.py collectstatic --noinput

# 6. Run the development server
python manage.py runserver 8001
```

### .env file

Create a `.env` file inside `student-attendance-frontend/`:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

---

## URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `home` | Dashboard |
| `/accounts/login/` | `CustomLoginView` | Login page |
| `/accounts/logout/` | `CustomLogoutView` | Logout |
| `/students/` | `students` | List all students |
| `/students/add/` | `add_student` | Add a student |
| `/students/edit/<id>/` | `edit_student` | Edit a student |
| `/students/delete/<id>/` | `delete_student` | Delete a student |
| `/teachers/` | `teachers` | List all teachers |
| `/teachers/add/` | `add_teacher` | Add a teacher |
| `/teachers/edit/<id>/` | `edit_teacher` | Edit a teacher |
| `/teachers/delete/<id>/` | `delete_teacher` | Delete a teacher |
| `/courses/` | `courses` | List all courses |
| `/courses/add/` | `add_course` | Add a course |
| `/courses/edit/<id>/` | `edit_course` | Edit a course |
| `/courses/delete/<id>/` | `delete_course` | Delete a course |
| `/attendance/` | `attendance` | List attendance records |
| `/attendance/add/` | `add_attendance` | Add attendance record |
| `/attendance/edit/<id>/` | `edit_attendance` | Edit attendance record |
| `/attendance/delete/<id>/` | `delete_attendance` | Delete attendance record |
| `/reports/` | `reports` | Attendance reports & statistics |

---

## Deployment (Render)

1. Push your code to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Set the following:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command:** `gunicorn frontend_project.wsgi:application`
   - **Root Directory:** `student-attendance-frontend`
4. Add environment variables in Render dashboard:

| Key | Value |
|---|---|
| `SECRET_KEY` | your secure secret key |
| `DEBUG` | `False` |

---

## Backend API

This frontend connects to the backend REST API at:

```
https://student-attendance-backend-h3hr.onrender.com/api
```

Endpoints used:

| Endpoint | Description |
|---|---|
| `/api/students/` | CRUD for students |
| `/api/teachers/` | CRUD for teachers |
| `/api/courses/` | CRUD for courses |
| `/api/attendance/` | CRUD for attendance records |

---

## License

MIT
