from rest_framework import serializers
from app.model.pages.user import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'