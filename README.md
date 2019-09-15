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

Now you have all tables created. Fill the API with data by running the setup script

```bash
$ ./setup.sh
```

Start the server

```bash
$ python manage.py runserver 
```

## Demo

The test server now runs at `http://localhost:8000`.   
You can access the various endpoints listed below

### Access Token

Before you can access the endpoints, you have to generate an access token. First, you need to create a real user by executing the command 
```bash
$ python manage.py createuser
```

Now, you can generate an access token by sending a `POST` request to `http://localhost:8000/auth/token` with params `{"username": "<your-username>", "password": "<your-password>"}`
You will get an access token and a refresh token.
The response should look similar to this

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU2ODU5NDUxMSwianRpIjoiZTVjMWNiMjBiOGY1NDE0YmE3N2ZmMjY4ODIzYWE5MzMiLCJ1c2VyX2lkIjoxMDN9.uH_gSN6O0_-tSUNxy7Zk2oLK_zvJDHXAOxU-6hqlApU",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY4NTA4NDExLCJqdGkiOiI4YTYyOThjYjA4Y2Q0NzE1YjQwNzU4ODU5OTU3Yzk3MyIsInVzZXJfaWQiOjEwM30.sUm54ozOWEL66VprJh8F_ikkhyrg8OkVYk2aPVXH6OM"
}
```

You can use the refresh token to get a new access token by sending a `POST` request to `http://localhost:8000/auth/token/refresh` with params `{"refresh": "<your-refresh-token>"}`

### Endpoints

Include your access token in the header `Authorization: Bearer <your-access-token>`

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
This project is published under the <a href="https://github.com/pr0grammr/mini-users-api/blob/master/LICENSE" title="MIT License">MIT License</a>

Feel free to extend the views, models or commands for personal use