from django.core.management import BaseCommand

from main.models import Students


class Command(BaseCommand):
    """
    кастомная команда для наполнения бд
    """

    def handle(self, *args, **options):
        """
        обязательная функция для работы команды
        :param args:
        :param options:
        :return:
        """
        student_list = [
            {'first_name': 'Ivanov', 'last_name': 'Ivan'},
            {'first_name': 'Petrov', 'last_name': 'Petr'},
            {'first_name': 'Sidorov', 'last_name': 'Sidr'},
        ]


        student_for_create = []
        for item in student_list:
            # наполнение списка через класс и единоразовая выгрузка его в бд
            student_for_create.append(
                Students(**item)
            )

        Students.objects.bulk_create(student_for_create)