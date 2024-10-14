import json

from django.core.management.base import BaseCommand

from books.converters import DateConverter
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

# Скрипт для заполнения локальной БД данными из json-файла
    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
        print(books)

        for book in books:
            Book.objects.create(
                name=book.get('fields').get('name'),
                author=book.get('fields').get('author'),
                pub_date=DateConverter().to_python(book.get('fields').get('pub_date'))

            )