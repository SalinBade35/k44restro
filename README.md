# Restaurant Management Website

A restaurant website built with Python and Django, using PostgreSQL as the database. The application provides user authentication, authorization, automated email notifications, and restaurant menu display.

## Features

* **User Authentication:** User registration, login, and logout using Django's built-in authentication system.
* **Authorization:** Access control using Django's built-in permissions and authentication features, as implemented in the project.
* **Email Notifications:** Automatically sends emails to users for configured application events.
* **Menu Display:** Displays restaurant menu items to users.
* **Database Management:** Stores application data using PostgreSQL.

## Technologies Used

* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS, JavaScript, Bootstrap (if used in the project)
* **Authentication:** Django Authentication System
* **Email:** Django Email Framework

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with your actual GitHub repository URL and project folder name.

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
```

**macOS / Linux:**

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the Database

Install PostgreSQL and create a database for the project.

Configure the database connection in your Django settings or environment variables according to the project's existing configuration.

### 6. Configure Environment Variables

Set the required database credentials and email settings according to your project configuration.

For email functionality, configure a valid email backend and the required credentials. Keep passwords and other secrets out of your public repository.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Screenshots

Add screenshots of the website to a `screenshots/` directory in your repository.

```markdown
![Restaurant Homepage](screenshots/home.png)
![Restaurant Menu](screenshots/menu.png)
```

## Requirements

* Python
* pip
* PostgreSQL
* Dependencies listed in `requirements.txt`

## Security Notes

* Do not commit database passwords, email credentials, or secret keys.
* Keep environment files such as `.env` out of version control.
* Use appropriate production settings before deploying the application.

## License

Specify a license if you intend to permit others to reuse or distribute this project.
