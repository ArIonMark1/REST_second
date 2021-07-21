from django.db import models
from authors.models import Author


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    release_year = models.PositiveIntegerField(verbose_name='Release Year')
    author = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.title}'
