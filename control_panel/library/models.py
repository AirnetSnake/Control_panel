# -*- encoding: utf-8 -*-
from django.db import models
from datetime import datetime

# Create your models here.

class Publisher(models.Model):
    title = models.CharField('Название', max_length=32)
    address = models.TextField('Адрес', null=True, blank=True)
    city = models.CharField('Город', max_length=64)
    country = models.CharField('Страна', max_length=64, null=True, blank=True)
    website = models.URLField('Адрес сайта', null=True, blank=True)

    def __unicode__(self):
	return u'%s (%s)' % (self.title, self.website)


class Author(models.Model):
    first_name = models.CharField('Имя', max_length=32)
    last_name = models.CharField('Фамилия', max_length=32)
    email = models.EmailField('Электронная почта', null=True, blank=True)

    def __unicode__(self):
	return u'%s %s' % (self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField('Название', max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField('Дата выпуска', default=datetime.now())

    def __unicode__(self):
	return u'%s' % (self.title)


