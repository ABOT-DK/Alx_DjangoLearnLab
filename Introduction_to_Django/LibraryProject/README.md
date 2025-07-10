
# Django Starter Project 🚀

This is a starter guide for setting up a Django project from scratch using the Django command-line interface through Python.

---

## 📦 Requirements

- Python 3.8 or higher
- pip (Python package manager)

---

## 🛠️ Setup Instructions

### 1. Install Django

```bash
pip install django
```

### 2. Create a Django Project

Navigate to your project directory and run:

```bash
python -m django startproject myproject .
```

> The `.` places the project files in the current directory rather than nesting them.

---

## 🧪 Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the default Django welcome page.

---

## ⚙️ Optional: Configure MySQL Database

1. **Install MySQL client:**

```bash
pip install mysqlclient
```

2. **Update your `settings.py` database config:**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

3. **Apply migrations:**

```bash
python manage.py migrate
```

---

## ✅ Common Commands

| Command                             | Description                      |
|------------------------------------|----------------------------------|
| `python manage.py runserver`       | Start the local server           |
| `python manage.py migrate`         | Apply database migrations        |
| `python manage.py createsuperuser` | Create an admin user             |
| `python manage.py startapp appname`| Create a new Django app          |

---

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [W3Schools Django Tutorial](https://www.w3schools.com/django/)
- [Real Python Django Guide](https://realpython.com/tutorials/django/)
