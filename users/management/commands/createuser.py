from django.core.management.base import BaseCommand
from getpass import getpass as password_input
from getpass import getpass as password_input
from users.models import User


class Command(BaseCommand):
    help = 'Creates a user'

    def handle(self, *args, **options):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        email = input('Enter email: ')
        username = input('Enter username: ')
        password = password_input('Enter password: ')

        try:
            User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
        except Exception as e:
            self.stderr.write('Could not create user: {}'.format(str(e)))

