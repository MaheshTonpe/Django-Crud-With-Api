from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField( null=True, blank=True )

    def __str__(self)->str:
        return self.title

class Meta:
    db_table = 'Book'

