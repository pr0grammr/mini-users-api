# Simple user REST API

Lightweight REST API example with users and associated posts, written in Python, <a href="https://www.djangoproject.com/" target="_blank" title="Django">Django</a> and <a href="https://www.django-rest-framework.org/" target="_blank" title="Django REST Framework">Django REST Framework</a>.   

You can use this project as a boilerplate for your own project.

## Requirements

- SQLite3
- Python
- Django
- pip

## Get started

Before you can run the API, open a terminal, change into the project root and execute the following commands to get started.

```bash
# install all dependencies
$ pip install requirements.txt

# create and run migrations for database
$ python manage.py makemigrations
$ python manage.py migrate
```

Now you have all tables created. Fill the API with data by running the following

```bash
# creates some user interests, e.g.: "Party", "Sports", "Art"
$ python manage.py createfakeinterests

# creates 100 fake users
$ python manage.py createfakeusers 100

# creates random number of fake posts for each user
$ python manage.py createfakeposts
```

Start the server

```bash
$ python manage.py runserver 
```

## Demo

The test server now runs at `http://localhost:8000`.   
You can access the various endpoints listed below

### Endpoints

#### /users
List all users

#### /users/1
List the user with the ID `1`

#### /users/1/posts
List all posts of user with ID `1`

## License
This project is published under the MIT License

Feel free to extend the views, models or commands for personal use