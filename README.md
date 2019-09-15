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

#### Users
`GET` `/users` - List all users   

`GET` `/users/1` - List the user by ID `1`  
`GET` `/users/1/posts` - List all posts of user by ID `1`  
`PUT` `/users/1` - Updates user by ID `1` with possible params

```json
{
  "username": "<updated-username>",
  "email": "<updated-email>",
  "first_name": "<updated-first-name>",
  "last_name": "<updated-last-name>"
}
```

`DELETE` `/users/1` - Deletes user by ID 1

#### Posts

`POST` `/posts` - Creates new post with params `{"text": "Updated post text"}`    

`GET` `/posts/10` - Get single post by ID  
`UPDATE` `/posts/10` - Updates post by ID `10` with params `{"text": "Updated post text"}`  
`DELETE` `/posts/10` - Deletes post by ID `10`

## License
This project is published under the MIT License

Feel free to extend the views, models or commands for personal use