# Create your views here.

from django.db import models
from datetime import datetime
from library.models import Book
from library.models import Author
from library.models import Publisher
from django.shortcuts import render

def get_book_list(request, sub):
	books = Book.objects.all()
	smth = {'books':books}
	return render(request, 'booklist.html', smth)

def get_book_info(request, sub):
	book = Book.objects.get(id=sub)
	smth = {'book':book, 'authors': book.authors.all()}
	return render(request, 'bookinfo.html', smth)

def get_authors(request):
	authors = Author.objects.all()	
	smth = {'authors':authors}
	return render(request, 'authors.html', smth)	

def get_author_info(request, sub):
	author = Author.objects.get(id=sub)	
	smth = {'author':author}
	return render(request, 'author.html', smth)
