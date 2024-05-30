from django.db import models

# Create your models here.

class Person(models.Model):
    u_name = models.CharField(max_length=50,null=True, blank=True)
    u_location = models.CharField(max_length=50, null=True, blank=True)
    u_email = models.EmailField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.u_name
    
    class Meta:
        db_table = 'Person'
        