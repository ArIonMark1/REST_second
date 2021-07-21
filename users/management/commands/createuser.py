# from abc import ABC

from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand
from users.models import BaseUser


# при вводе команды: createuser -p username = создает пользователя с именем "username"
# при вводе команды: createuser -p username -a = создает суперпользователя с именем "username"
# при вводе команды: createuser или createuser -a = создает пользователя/суперпользователя с рандомным именем

class Command(BaseCommand):
    help = '=== create user or superuser ==='

    def add_arguments(self, parser):
        parser.add_argument('-p', '--prefix', type=str, help='define a username prefix')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **options):
        prefix = options['prefix']
        admin = options['admin']

        if prefix:
            username = f'{prefix}'
        else:
            username = f'{get_random_string()}'

        if admin:
            BaseUser.objects.create_superuser(username=username,
                                              email=f'{input("Enter your Email: ")}',
                                              password=f'{input("Enter password: ")}')

            self.stdout.write(self.style.SUCCESS(f'Successfully created user: "{username}"'))
        else:
            BaseUser.objects.create_user(username=username,
                                         email=f'{input("Enter your Email: ")}',
                                         password=f'{input("Enter password: ")}')

            self.stdout.write(self.style.SUCCESS(f'Successfully created user: "{username}"'))
