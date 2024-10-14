from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'

    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_pagi(request, input_date):
    template = 'books/books_list.html'

    books = Book.objects.all()



    context = {'books': books}
    return render(request, template, context)