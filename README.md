# Job Application Form

This project is a web application built with Django that allows users to submit a job application form. The application includes features like form submission, email confirmation, and an admin interface for managing submitted forms. 

## Features

- **Form Submission:** Users can submit a job application form with details such as first name, last name, email, start date, and occupation.
- **Email Confirmation:** After form submission, the user receives a confirmation email with their submitted details.
- **Admin Interface:** Admins can view and manage submitted forms.

## Technologies Used

- **Django:** A high-level Python web framework for rapid development.
- **Bootstrap:** A front-end framework for responsive design.
- **SQLite:** A lightweight, disk-based database.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- SQLite

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/job-application-form.git
    cd job-application-form
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your environment variables:
    ```plaintext
    SECRET_KEY=your_secret_key
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_email_password
    ```

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser to access the admin interface:
    ```sh
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```sh
    python manage.py runserver
    ```

8. Access the application in your web browser at `http://127.0.0.1:8000`.

## Project Structure

```plaintext
job-application-form/
├── job_application/
│   ├── migrations/
|   |   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── templates/
│   │   ├── about.html
│   │   ├── base.html
|   |   ├── contact.html
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Usage
### Admin Interface
1. Log in to the admin interface at http://127.0.0.1:8000/admin. 
2. Use the superuser credentials you created during setup. 
3. Manage submitted forms and other site data. 

## Navigating the Site
- Home Page: Access the job application form.
- Contact Page: Find contact information.
- Admin Interface: Manage form submissions and other data.

## Attachments
![image](https://github.com/FriendlyMaabuat/Django-WebApp/assets/92776515/6289891a-bd4e-4001-b723-c5db0cae6c70)
![image](https://github.com/FriendlyMaabuat/Django-WebApp/assets/92776515/0ab3a427-707a-4bbb-934f-cd74442199b1)


