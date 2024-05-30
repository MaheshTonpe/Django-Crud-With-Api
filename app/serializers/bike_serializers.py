from rest_framework import serializers
from app.model.pages.bike import Bike

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'