from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.serializers.employee_serializers import EmployeeSerializer
from app.model.pages.employee import Employee

class EmployeeView(ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        result = map_employee_object(queryset)
        return Response(result)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Employee created successfully")
    
    def edit(self, request, pk):
        row = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        row.e_name = serializer.data.get('e_name')
        row.e_location = serializer.data.get('e_location')
        row.e_email = serializer.data.get('e_email')
        row.save()
        return Response("Employee updated successfully")
    
    def retrieve(self, request, pk):
        row = Employee.objects.get(pk=pk)
        row = transform_signal(row)
        return Response(row)

    def destroy(self, request, pk):
        row = Employee.objects.get(pk=pk)
        row.delete()
        return Response("Employee deleted successfully")



def transform_signal(instance):
    data_dict = {}
    data_dict['id'] = instance.id
    data_dict["e_name"] = instance.e_name
    data_dict["e_location"] = instance.e_location
    data_dict["e_email"] = instance.e_email
    return data_dict

def map_employee_object(data):
    return map(transform_signal, data)