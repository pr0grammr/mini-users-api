from django.core.management.base import BaseCommand
from random import randint
from users.models import User, Interest
from posts.models import Post
from faker import Faker
from core.management.commands.utils import get_random_values_from_list


class Command(BaseCommand):
    help = 'Creates fake posts for each user'

    def handle(self, *args, **options):
        f = Faker()
        posts = 0

        users = User.objects.all()
        for user in users:

            post_amount_per_user = randint(1, 5)

            for i in range(0, post_amount_per_user):
                tags = Interest.objects.values('id')
                tags = [Interest.objects.get(pk=tag['id']) for tag in tags]
                random_tags = get_random_values_from_list(tags)

                post = Post.objects.create(
                    text=f.text(),
                    user=user
                )

                for random_tag in random_tags:
                    post.tags.add(random_tag)

                post.save()
                posts += 1

            self.stdout.write(self.style.SUCCESS('Created {} posts for user {}'.format(post_amount_per_user, user.username)))
        self.stdout.write(self.style.SUCCESS('{} posts created'.format(posts)))
