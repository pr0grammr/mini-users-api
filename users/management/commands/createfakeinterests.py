from django.core.management.base import BaseCommand
from core.management.commands.utils import get_random_values_from_list
from users.models import Interest


class Command(BaseCommand):

    FAKE_INTERESTS = [
        ('sports', 'Sports'),
        ('programming', 'Programming'),
        ('party', 'Party'),
        ('travel', 'Travel'),
        ('hiking', 'Hiking'),
        ('art', 'Art'),
        ('football', 'Football'),
        ('formula1', 'Formula 1')
    ]

    def handle(self, *args, **options):

        for interest in self.FAKE_INTERESTS:
            name, value = interest

            Interest.objects.create(name=name, value=value)
            self.stdout.write(self.style.SUCCESS('Imported interest: {}'.format(value)))
        self.stdout.write(self.style.SUCCESS('Imported {} interests'.format(len(self.FAKE_INTERESTS))))
