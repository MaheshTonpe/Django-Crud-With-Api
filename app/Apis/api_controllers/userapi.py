from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.serializers.user_serializers import PersonSerializer
from app.model.pages.user import Person

class PersonView(ViewSet):
    def list(self, request):
        queryset = Person.objects.all()
        result = map_person_object(queryset)
        return Response(result)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("User created successfully")
    
    def edit(self, request, pk):
        row = Person.objects.get(pk=pk)
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        row.u_name = serializer.data.get('u_name')
        row.u_location = serializer.data.get('u_location')
        row.u_email = serializer.data.get('u_email')
        row.save()
        return Response("User updated successfully")
    
    def retrieve(self, request, pk):
        row = Person.objects.get(pk=pk)
        row = transform_signal(row)
        return Response(row)

    def destroy(self, request, pk):
        row = Person.objects.get(pk=pk)
        row.delete()
        return Response("User deleted successfully")



def transform_signal(instance):
    data_dict = {}
    data_dict['id'] = instance.id
    data_dict["u_name"] = instance.u_name
    data_dict["u_location"] = instance.u_location
    data_dict["u_email"] = instance.u_email
    return data_dict

def map_person_object(data):
    return map(transform_signal, data)