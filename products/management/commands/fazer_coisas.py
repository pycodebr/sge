from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('COISAS FEITAS COM SUCESSO!')
        )
