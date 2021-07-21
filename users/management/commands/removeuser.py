from django.core.management.base import BaseCommand
from users.models import BaseUser


# command: python manage.py removeuser user_id = delete user by ID 'user_id'
# command: python manage.py removeuser u_id-1 u_id-2 = delete users bu ID 'u_id-1' and 'u_id-2'

class Command(BaseCommand):
    help = '=== Delete user by ID ==='

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='Insert some user id')

    def handle(self, *args, **options):

        for user in options['user_id']:
            try:
                BaseUser.objects.get(pk=user).delete()
                self.stdout.write(self.style.SUCCESS(f' Successfully deleted user: "{user}"'))

            except BaseUser.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'User does not exist: "{user}"'))
