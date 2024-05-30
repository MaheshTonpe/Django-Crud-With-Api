from django.contrib import admin
from app.model.pages.books import Book
from app.model.pages.car import Car
from app.model.pages.employee import Employee
from app.model.pages.user import Person

# Register your models here.

admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Car)
admin.site.register(Book)