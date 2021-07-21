from django.core.management.base import BaseCommand
from users.models import BaseUser


class Command(BaseCommand):
    help = '=== make the user inactive ==='

    def add_arguments(self, parser):
        parser.add_argument('users_id', nargs='+',
                            type=int,
                            help='Toggles user activity to inactive mode like: " python manage.py inactiveuser user_id " ')

    def handle(self, *args, **options):

        for user_id in options['users_id']:
            try:
                user = BaseUser.objects.get(pk=user_id)
                user.is_active = False
                user.save()
            except BaseUser.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'USER WIDTH ID {user_id}  does not EXIST !!!'))

            self.stdout.write(self.style.SUCCESS(f'USER "{user.username}" IS INACTIVE'))
