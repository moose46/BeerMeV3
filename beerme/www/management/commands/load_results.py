from django.core.management.base import BaseCommand, CommandError
from www.models import Result


# https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        results = Result.objects.all()
        print(f"# of results = {results.count()}")
