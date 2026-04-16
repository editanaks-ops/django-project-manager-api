# Django Project Manager API

REST API for managing projects and tasks with role-based access control and token authentication.

##  Features

* CRUD operations for Projects and Tasks
* Token Authentication (Django REST Framework)
* Role-based permissions:

  * Anyone can read (GET)
  * Only staff users (Admin/Manager) can create, update, delete
* Custom permission class (`IsAdminOrManagerOrReadOnly`)
* API testing with Postman

##  Tech Stack

* Python 3
* Django
* Django REST Framework
* SQLite (default)

##  Authentication

This project uses Token Authentication.

Example header:

```
Authorization: Token your_token_here
```

##  API Endpoints

### Projects

* `GET /projects/api/projects/` — list projects
* `POST /projects/api/projects/` — create project (staff only)

### Tasks

* `GET /projects/api/tasks/` — list tasks
* `POST /projects/api/tasks/` — create task (staff only)

##  Testing (Postman)

1. Add header:

```
Authorization: Token your_token_here
```

2. For POST requests:

* Body → raw → JSON

Example:

```json
{
  "title": "Trip to Italy",
  "description": "My dream journey"
}
```

##  Setup

```bash
git clone https://github.com/your-username/django-project-manager-api.git
cd django-project-manager-api

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

##  Roles

| Role  | Permissions |
| ----- | ----------- |
| User  | Read only   |
| Staff | Full access |

##  Project Structure

```
projects/   # main app
users/      # authentication and user management
```


