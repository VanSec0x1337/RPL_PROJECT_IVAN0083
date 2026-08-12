<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=800&size=40&duration=3000&pause=1000&color=A855F7&center=true&vCenter=true&width=850&lines=RPL+PROJECT;Django+Student+Management;CRUD+Web+Application;Responsive+Web+Application" alt="RPL Project">

<p>
<strong>Django Student Management System</strong>
</p>

<p>
A Django-based web application for managing student data with authentication, CRUD operations, form validation, audio support, and responsive design.
</p>

<p>
<a href="https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/">
<img src="https://img.shields.io/badge/Live%20Website-A855F7?style=for-the-badge&logo=django&logoColor=white" alt="Live Website">
</a>
</p>

</div>

---

## About

RPL Project is a Software Engineering practical project built using Django.

The application provides a student management system with authentication and CRUD operations for creating, viewing, updating, and deleting student data.

Users must log in before accessing the student management system. After authentication, users can manage student records and access additional features such as audio playback and responsive layouts.

## Project Objectives

* Implement authentication using Django
* Manage student data through CRUD operations
* Validate user input through Django forms
* Build a responsive web interface
* Practice Django application structure and routing
* Deploy the application to a production environment

---

## Features

| Feature                | Description                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| **Authentication**     | Django authentication protects access to the student management system. |
| **Student Management** | View and manage student records stored in the database.                 |
| **Create**             | Add new student records through an input form.                          |
| **Update**             | Edit existing student information.                                      |
| **Delete**             | Remove student records from the system.                                 |
| **Form Validation**    | Validate input and display understandable error messages.               |
| **Audio Player**       | Background music player with play and pause controls.                   |
| **Responsive Design**  | Interface adapts to different screen sizes and devices.                 |

---

## Application Pages

| Page               | Function                                            |
| ------------------ | --------------------------------------------------- |
| **Login**          | Authenticate users before accessing the system      |
| **Home**           | Display application welcome information and summary |
| **Student List**   | Display all registered student data                 |
| **Add Student**    | Add a new student record                            |
| **Edit Student**   | Update existing student information                 |
| **Delete Student** | Remove a student record                             |
| **Logout**         | Safely end the current session                      |

---

## Technology Stack

| Technology                  | Purpose                                      |
| --------------------------- | -------------------------------------------- |
| **Python**                  | Main programming language                    |
| **Django 5.1.2**            | Web application framework                    |
| **SQLite**                  | Local database                               |
| **Gunicorn**                | Production WSGI server                       |
| **WhiteNoise**              | Static file serving                          |
| **dj-database-url**         | Database configuration                       |
| **PostgreSQL Support**      | Production database compatibility            |
| **HTML / CSS / JavaScript** | Frontend structure, styling, and interaction |

### Dependencies

The project uses the following main packages:

```text
Django==5.1.2
gunicorn
whitenoise
dj-database-url
psycopg2-binary
```

---

## Website Preview

<div align="center">

### Login Page

<a href="https://cdn.corenexis.com/f/FskQ1KtYugg.png">
<img src="https://cdn.corenexis.com/f/FskQ1KtYugg.png" alt="RPL Project Login Page" width="850">
</a>

<p>
<sub>Login page displayed before accessing the student management system.</sub>
</p>

<br>

### Dashboard

<a href="https://cdn.corenexis.com/f/FPypwvKEImV.png">
<img src="https://cdn.corenexis.com/f/FPypwvKEImV.png" alt="RPL Project Dashboard" width="850">
</a>

<p>
<sub>Main dashboard displayed after successful authentication.</sub>
</p>

</div>

---

## Data Model

The main model used by the application is `Mahasiswa`.

| Field          | Type        | Description                                                     |
| -------------- | ----------- | --------------------------------------------------------------- |
| `nim`          | `CharField` | Student identification number, maximum 15 characters and unique |
| `nama`         | `CharField` | Student name, maximum 100 characters                            |
| `programstudi` | `CharField` | Study program, maximum 50 characters                            |

---

## Project Structure

```text
RPL_PROJECT_IVAN0083/
│
├── accounts/
│   ├── templates/
│   │   └── accounts/
│   │       └── login.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── mahasiswa/
│   ├── migrations/
│   ├── static/
│   │   └── mahasiswa/
│   │       ├── audio/
│   │       │   └── music.mp3
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── img/
│   │       │   └── bahlil.gif
│   │       └── js/
│   │           └── main.js
│   │
│   ├── templates/
│   │   └── mahasiswa/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── daftar.html
│   │       ├── tambah.html
│   │       └── edit.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── rpl_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── Procfile
```

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/VanSec0x1337/RPL_PROJECT_IVAN0083.git
cd RPL_PROJECT_IVAN0083
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Create Your Own User

The project does not require a default account from the project owner.

For local development, create your own Django account:

```bash
python manage.py createsuperuser
```

Django will ask for:

```text
Username:
Email address:
Password:
Password (again):
```

Use your own username and password.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/accounts/login/
```

Log in using the account you created.

---

## Creating a Regular User

If you only need an account for application login without administrator access, use the Django shell:

```bash
python manage.py shell
```

Then:

```python
from django.contrib.auth.models import User

User.objects.create_user(
    username="demo",
    email="demo@example.com",
    password="PasswordDemo123!"
)
```

Exit the shell:

```python
exit()
```

You can then log in using the credentials you created.

> Do not commit real passwords to the repository. The example credentials above are only for local demonstration.

---

## Live Demo

The live website is available at:

<a href="https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/">
https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/
</a>

For the live deployment, available accounts depend on the deployment database.

This README does not provide the project owner's credentials. Users who want to test the live application need an account available in the deployment environment.

---

## Application Flow

```text
Login
  ↓
Dashboard / Home
  ↓
Student List
  ↓
┌───────────────┬───────────────┐
│     Create    │     Update    │
└───────────────┴───────────────┘
          ↓
    Student Data
          ↓
        Delete
```

---

## Security

The application uses Django authentication to restrict access to the student management pages.

Protected views use `login_required`, requiring users to authenticate before accessing the main student management features.

The authentication system uses Django's username and password mechanism. Users can create their own accounts using `createsuperuser` or the Django shell.

POST forms also use Django's built-in CSRF protection.

---

## Deployment

The application is configured for deployment using Python web hosting infrastructure.

The project includes:

* `gunicorn` for the WSGI server
* `whitenoise` for static files
* `dj-database-url` for database configuration
* `psycopg2-binary` for PostgreSQL support
* `Procfile` for deployment configuration

---

## Live Website

<div align="center">

<a href="https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/">
<img src="https://img.shields.io/badge/Open%20Live%20Website-A855F7?style=for-the-badge&logo=django&logoColor=white" alt="Open Live Website">
</a>

<br><br>

<strong>RPL Project — Django Student Management System</strong>

<br>

<sub>Software Engineering practical project</sub>

</div>

---

## Author

<div align="center">

<strong>Ivan Surya Buwana</strong>

G.211.24.0083 · Teknik Informatika

<br><br>

<a href="https://github.com/VanSec0x1337">
<img src="https://img.shields.io/badge/GitHub-VanSec0x1337-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>

<br><br>

Build · Learn · Improve · Repeat

<br><br>

© 2026 RPL Project · Ivan Surya Buwana

</div>
