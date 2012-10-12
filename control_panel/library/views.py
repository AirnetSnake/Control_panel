# Create your views here.

from django.db import models
from datetime import datetime

def get_book_list(request):
    book_list = Person.objects.all()[-1]
    return book_list.title, book_list.author, book_list.publisher 

