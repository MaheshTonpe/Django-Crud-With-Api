from django.db import models

# Create your models here.

class Car(models.Model):
    brand_name = models.CharField(max_length=50, blank=True, null=True )
    model_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField( blank=True, null=True, default=0 )
    
    def __str__(self) -> str:
        return self.brand_name
    
    class Meta:
        db_table = 'Car'