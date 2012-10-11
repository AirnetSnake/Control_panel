# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.

class Publisher(models.Model):
    title = models.CharField('Название', max_length=32)
    address = models.TextField('Адрес')
    city = models.CharField('Город', max_length=64)
    country = models.CharField('Страна', max_length=64)
    website = models.URLField('Адрес сайта')

class Author(models.Model):
    first_name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    email = models.EmailField('Электронная почта', null=True)

class Book(models.Model):
    title = models.CharField('Название', max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField('Дата выпуска', default=datetime.now())

def __unicode__(self):
	if type(self) is Author:
        	return u'%s %s' % (self.last_name, self.first_name)
	elif type(self) is Book:
		return u'%s' % (self.title)
	elif type(self) is Publisher:
		return u'%s (%s)' % (self.title, self.website)


