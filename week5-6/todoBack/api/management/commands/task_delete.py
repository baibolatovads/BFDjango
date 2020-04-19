from django.core.management.base import BaseCommand
from datetime import datetime
import random

from api.models import Task, TaskList


class Command(BaseCommand):
    help = 'Delete Task objects from table'

    def add_arguments(self, parser):
        parser.add_argument('task_ids', nargs='+', help='Task ids for delete')

    def handle(self, *args, **kwargs):

        for task_id in kwargs['task_ids']:
            try:
                t = Task.objects.get(id=task_id)
                t.delete()
                self.stdout.write(self.style.SUCCESS("Task id: {} deleted successfully".format(task_id)))
            except Task.DoesNotExist as e:
                self.stdout.write(self.style.ERROR("Task id: {} does not exist!".format(task_id)))