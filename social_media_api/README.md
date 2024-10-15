# Social Media API

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)


## Project Overview
The Social Media API is a robust backend solution designed for a social media platform, built using Django and Django REST Framework. This API allows users to create, view, like, comment on posts, follow other users, and receive notifications. It provides a comprehensive and scalable structure for developing social networking applications.

## Features
- **User Authentication**: Secure user registration, login, and profile management.
- **Posts and Comments**: Users can create, read, update, and delete posts and comments.
- **Likes Functionality**: Users can like and unlike posts, with notifications generated for likes.
- **User Follows**: Users can follow and unfollow others, with a dynamic feed of posts from followed users.
- **Notifications**: Users receive notifications for various interactions, enhancing engagement.
- **Advanced Search and Filtering**: Easily search for posts by title or content.

## Technologies Used
- Python 3.x
- Django 4.x
- Django REST Framework
- PostgreSQL / MySQL (Database)
- Nginx (Web Server)
- Gunicorn (WSGI Server)
- AWS S3 (for static/media file storage, optional)

## Installation

### Prerequisites
- Python 3.x installed
- pip (Python package manager)
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/social_media_api.git
   cd social_media_api


2. Create and activate a virtual environment:
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install the required packages:
     pip install -r requirements.txt

4. Set up the database:
     Update the DATABASES setting in settings.py with your database credentials.
     Run migrations:
      python manage.py migrate

5. Create a superuser for the admin interface:
        python manage.py createsuperuser   

6. Run the server:
       python manage.py runserver



 Usage
Access the API at http://localhost:8000/api/.
Use tools like Postman to test the endpoints.
API Endpoints
Authentication
POST /api/auth/register/ - User registration
POST /api/auth/login/ - User login
POST /api/auth/logout/ - User logout
Posts
GET /api/posts/ - List all posts
POST /api/posts/ - Create a new post
GET /api/posts/<int:pk>/ - Retrieve a specific post
PUT /api/posts/<int:pk>/ - Update a specific post
DELETE /api/posts/<int:pk>/ - Delete a specific post
POST /api/posts/<int:pk>/like/ - Like a specific post
POST /api/posts/<int:pk>/unlike/ - Unlike a specific post
Comments
GET /api/posts/<int:pk>/comments/ - List comments for a post
POST /api/posts/<int:pk>/comments/ - Create a new comment on a post
PUT /api/comments/<int:pk>/ - Update a specific comment
DELETE /api/comments/<int:pk>/ - Delete a specific comment
User Follows
POST /api/follow/<int:user_id>/ - Follow a user
POST /api/unfollow/<int:user_id>/ - Unfollow a user
GET /api/feed/ - Get the feed of posts from followed users
Notifications
GET /api/notifications/ - List notifications for the user
Deployment
For deployment instructions, refer to the Deployment section in this README.

Testing
To run tests, execute the following command:
    python manage.py test


Contributing
Contributions are welcome! Please fork the repository and submit a pull request. Ensure your code adheres to the project's style guidelines.


Feel free to modify any section to better fit your project’s specifics!

