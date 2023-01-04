from django.shortcuts import render
from readlist_app.models import Book
from django.http import JsonResponse

def book_list(request):
    books = Book.objects.all()
    data = {'movies':list(books.values())}
    return JsonResponse(data)
