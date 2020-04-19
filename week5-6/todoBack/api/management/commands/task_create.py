from django.core.management.base import BaseCommand
from datetime import datetime
import random

from api.models import Task, TaskList


def create_task_list(num=3):
    task_lists = [TaskList(topic='Task List{}'.format(i))
               for i in range(num)]

    TaskList.objects.bulk_create(task_lists)


class Command(BaseCommand):
    help = 'Create fake date for Task table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of tasks for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new tasks')


    def handle(self, *args, **kwargs):
        # Task.objects.all().delete()

        total = kwargs['total']
        prefix = kwargs.get('prefix')

        if not prefix:
            prefix = 'My'

        create_task_list(total)

        #self.stdout.write()
        for i in range(total):
            t = Task.objects.create(name=f'{prefix}_task {i}')
            self.stdout.write(f'Task {t.id} created')

