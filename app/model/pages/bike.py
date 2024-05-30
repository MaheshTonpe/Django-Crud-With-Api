
from django.db import models

class Bike(models.Model):
    brand_name = models.CharField(max_length=50, blank=True, null=True )
    model_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField( blank=True, null=True, default=0 )

def __str__(self):
    return self.brand_name

class Meta:
    db_table = 'Bike'

