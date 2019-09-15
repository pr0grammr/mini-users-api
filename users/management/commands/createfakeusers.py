from django.core.management.base import BaseCommand
from faker import Faker
from users.models import User, Interest
from random import randint
from core.management.commands.utils import get_random_values_from_list


class Command(BaseCommand):
    help = 'Creates fake users by given amount'

    EMAIL_TLDS = [
        'gmail.com',
        'web.de',
        'gmx.net'
    ]

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='number of users to create')

    def handle(self, *args, **options):
        f = Faker()

        for i in range(0, options['amount']):

            first_name, last_name = self._build_name_components(f.name())
            email = self._build_random_email(first_name=first_name, last_name=last_name)

            interests = Interest.objects.values('id')
            interests = [Interest.objects.get(pk=interest['id']) for interest in interests]
            random_interests = get_random_values_from_list(interests)

            user = User.objects.create_user(
                username='{}.{}'.format(first_name.lower(), last_name.lower()),
                email=email,
                password=f.password(),
                first_name=first_name,
                last_name=last_name
            )

            for random_interest in random_interests:
                user.interests.add(random_interest)

            user.save()
            self.stdout.write(self.style.SUCCESS('Created user {}'.format(email)))
        self.stdout.write(self.style.SUCCESS('Created {} fake users'.format(options['amount'])))


    def _get_random_value(self, lst):
        return lst[randint(0, len(lst) -1 )]

    def _build_random_email(self, **kwargs):
        return '{}.{}@{}'.format(kwargs['first_name'].lower(), kwargs['last_name'].lower(), self._get_random_value(self.EMAIL_TLDS))

    def _build_name_components(self, name):
        name_components = name.split(' ')
        first_name = ' '.join(name_components[:-1])
        last_name = name_components[-1]

        return first_name, last_name

