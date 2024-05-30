from django.db import models

# Create your models here.

class Employee(models.Model):
    e_name = models.CharField(max_length=50, blank=True, null=True)
    e_location = models.CharField(max_length=50, blank=True, null=True)
    e_email = models.EmailField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.e_name
    
    class Meta:
        db_table = 'Employee'