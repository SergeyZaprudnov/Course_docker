from django.core.management import BaseCommand
from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_check_1 = Users.objects.filter(email="test@test.com")
        if not user_check_1:
            user = Users.objects.create(
                email="test@test.com",
                first_name="test@test.com",
                last_name="test@test.com",
                telegram_user_name="Evers",
                is_superuser=True,
                is_staff=True,
                is_active=True
                )

            user.set_password("test")
            user.save()

        user_check_2 = Users.objects.filter(email="test@test.com")
        if not user_check_2:
            user = Users.objects.create(
                email="test@test.com",
                first_name="test@test.com",
                last_name="test@test.com",
                telegram_user_name="Sors",
                is_superuser=False,
                is_staff=False,
                is_active=True
            )

            user.set_password("test")
            user.save()
