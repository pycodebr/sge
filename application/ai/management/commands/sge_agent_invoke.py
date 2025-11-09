from django.core.management.base import BaseCommand
from ai.agent import SGEAgent


class Command(BaseCommand):

    def handle(self, *args, **options):
        agent = SGEAgent()
        agent.invoke()

        self.stdout.write(
            self.style.SUCCESS('SGE AGENT INVOCADO COM SUCESSO!')
        )
