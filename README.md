# Django CRUD Application

CRUD operations (Create, Read, Update, Delete) are fundamental in database management. This project is a Django web application designed to perform CRUD operations on a demo **Student** model. The project is now complete.

## Features 

- **Create**: Add new student entries to the database.
- **Read**: View and retrieve student details.
- **Update**: Edit the existing student information.
- **Delete**: Remove student records from the database.

## Tech Stack

- **Frontend**: Django Templates (HTML, CSS, JavaScript)
- **Backend**: Django (Python)
- **Database**: SQLite (default with Django)

## Current Status

The project is complete now. Below is a breakdown of the progress made:
- [x] Set up the Django project structure.
- [x] Basic configuration and installation.
- [x] Defined the **Student** model.
- [x] Create functionality.
- [x] Read functionality.
- [x] Update functionality (pending).
- [x] Delete functionality (pending).

## Installation (for testing the current progress)

1. Clone the repository:
   ```bash
   git clone https://github.com/Godvein/Django-CRUD.git
   
Once cloned, navigate to the project directory:

```bash
cd CRUD
```

### Step 2: Set Up a Virtual Environment

It is recommended to use a virtual environment to manage your project dependencies.

1. Install `pipenv` if you don’t have it installed:

    ```bash
    pip install pipenv
    ```

2. Create a virtual environment and activate it:

    ```bash
    pipenv shell
    ```

If you're not using `pipenv`, you can use `venv` instead:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
.\venv\Scripts\activate   # For Windows
```

### Step 3: Install Dependencies

If you're using `pipenv`, install the dependencies from the `Pipfile`:

```bash
pipenv install
```

Alternatively, if you're using `venv`, install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Database

By default, this project uses SQLite, which comes pre-installed with Django. There is no need for extra configuration for SQLite.

If you want to use a different database (such as PostgreSQL or MySQL), you will need to configure the database settings in the `settings.py` file and install the necessary database adapters.

### Step 5: Run Database Migrations

To set up the database schema, run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the necessary tables in your SQLite database (or the database of your choice).

### Step 6: Create a Superuser (Admin)

To access the Django admin panel, you'll need to create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

### Step 7: Run the Development Server

To start the Django development server, use the following command:

```bash
python manage.py runserver
```

Once the server is running, visit `http://127.0.0.1:8000/` in your web browser to access the application.

You can also visit the admin interface at `http://127.0.0.1:8000/admin/` using the superuser credentials created earlier.

## Optional: Deactivate the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

If you’re using `pipenv`, simply exit the shell:

```bash
exit
```

## License

This project is licensed under the MIT License.
```

This complete installation guide provides all the necessary steps for setting up your Django CRUD application, formatted in markdown.
