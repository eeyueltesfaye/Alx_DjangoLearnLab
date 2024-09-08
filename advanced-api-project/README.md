Advanced API Project
Overview
This project demonstrates an advanced API using Django REST Framework. It includes functionalities such as CRUD operations for a Book model, filtering, searching, ordering, and permission management for API endpoints.

Features
CRUD operations for the Book model (Create, Retrieve, Update, Delete)
Filtering, searching, and ordering books by title, author, and publication year
Custom serializers for nested relationships between Author and Book
Comprehensive unit tests to ensure functionality
Permissions to restrict access based on authentication
Requirements
Python 3.8+
Django 4.x+
Django REST Framework
django-filter
Installation
Clone the repository:
bash
Copy code
git clone <repository-url>
cd advanced_api_project
Create a virtual environment and install the dependencies:
bash
Copy code
python -m venv env
source env/bin/activate  # For Windows use: env\Scripts\activate
pip install -r requirements.txt
Run migrations to set up the database:
bash
Copy code
python manage.py migrate
Create a superuser for accessing the admin:
bash
Copy code
python manage.py createsuperuser
Start the development server:
bash
Copy code
python manage.py runserver
Testing
Test Setup
For testing, Django's built-in testing framework is used, which is based on Python's unittest module. The test cases are defined in api/tests.py.

Important: Django automatically uses a separate test database, so running tests won’t affect your development or production data.

Configure Settings for Testing
To ensure that the test environment is isolated, make sure the following is in your settings.py file:

python
Copy code
# settings.py

# Database setup for tests (Django handles test databases automatically)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticatedOrReadOnly'],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',  # To use JSON as default format for tests
}
How to Run Tests
You can run the test suite using Django's manage.py command. Navigate to the root directory of your project (where manage.py is located) and run:

bash
Copy code
python manage.py test api
This will run all the test cases defined in the api/tests.py file.

Test Coverage
The test suite includes the following:

CRUD Operations: Tests for creating, retrieving, updating, and deleting Book objects.
Filtering, Searching, and Ordering: Tests that ensure API filtering, searching, and ordering by attributes like title, author, and publication year work correctly.
Permissions: Tests to ensure that only authenticated users can create, update, or delete books, while anyone can retrieve a list of books.
Response Codes and Data: Tests ensure that the correct status codes and response data are returned for all API requests.
API Endpoints
Method	Endpoint	Description
GET	/books/	List all books
POST	/books/	Create a new book (auth required)
GET	/books/<id>/	Retrieve details of a book
PUT	/books/<id>/	Update a book (auth required)
DELETE	/books/<id>/	Delete a book (auth required)
Filtering, Searching, and Ordering
Filtering: Filter books by title, author, and publication year.
Searching: Search books by title or author.
Ordering: Order books by title or publication year.
Example usage:

Filtering: /books/?title=Test Book
Searching: /books/?search=Author Name
Ordering: /books/?ordering=publication_year
Running the Project
Start the development server:
bash
Copy code
python manage.py runserver
Access the API at: http://127.0.0.1:8000/books/
This README provides clear steps to install, configure, and test the project, with instructions on how to add necessary settings and run tests.

Additional Notes:
Django Test Database: Django automatically creates a separate test database, so no additional configuration is needed unless you want to customize it.
Test Result Interpretation: When you run tests, you'll see a summary of passed/failed tests. If any tests fail, Django will give you detailed error messages.