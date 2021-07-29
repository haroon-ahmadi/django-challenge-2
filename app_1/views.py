from django.http import HttpResponse
from django.shortcuts import redirect, render

from app_1.models import Book, Author


def home_page(request):
    return redirect('book_list')


def book_list(request):
    author_name = request.GET.get('author_name')

    if author_name:
        try:
            author = Author.objects.get(name=author_name)
            books = Book.objects.filter(author=author).all()
        except:
            books = []
    else:
        books = Book.objects.all()

    context = {'books': books, 'author_name': author_name}
    return render(request, 'book_list.html', context, status=200)
