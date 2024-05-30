from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.serializers.bike_serializers import BikeSerializer
from app.model.pages.bike import Bike

class BikeView(ViewSet):

    def list(self, request):
        queryset = Bike.objects.all()
        result = map_bike_object(queryset)
        return Response(result)

    def create(self, request):
        serializer = BikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Bike created successfully")
    
    def edit(self, request, pk):
        row = Bike.objects.get(pk=pk)
        serializer = BikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        row.brand_name = serializer.data.get('brand_name')
        row.model_name = serializer.data.get('model_name')
        row.price = serializer.data.get('price')
        row.save()
        return Response("Bike updated successfully")
    
    def retrieve(self, request, pk):
        row = Bike.objects.get(pk=pk)
        row = transform_signal(row)
        return Response(row)

    def destroy(self, request, pk):
        row = Bike.objects.get(pk=pk)
        row.delete()
        return Response("Bike deleted successfully")

def transform_signal(instance):
    data_dict = {}
    data_dict['id'] = instance.id
    data_dict["brand_name"] = instance.brand_name
    data_dict["model_name"] = instance.model_name
    data_dict["price"] = instance.price
    return data_dict

def map_bike_object(data):
    return map(transform_signal, data)