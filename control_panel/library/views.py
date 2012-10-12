# Create your views here.

<<<<<<< HEAD
from myapp.models import Person
 
def get_last_person_name(request):
    last_person = Person.objects.all()[-1]
    return last_person.name
=======
from django.db import models
from datetime import datetime

def get_book_list(request):
    book_list = Person.objects.all()[-1]
    return book_list.title, book_list.author, book_list.publisher 
>>>>>>> 4.1.1
