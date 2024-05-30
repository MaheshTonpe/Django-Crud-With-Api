from rest_framework import serializers
from app.model.pages.books import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'