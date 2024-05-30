from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.serializers.books_serializers import BookSerializer
from app.model.pages.books import Book


class BookView(ViewSet):

    def list(self, request):
        queryset = Book.objects.all()
        result = map_book_object(queryset)
        return Response(result)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Book created successfully")
    
    def edit(self, request, pk):
        row = Book.objects.get(pk=pk)
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        row.title = serializer.data.get('title')
        row.author = serializer.data.get('author')
        row.price = serializer.data.get('price')
        row.save()
        return Response("Book updated successfully")
    
    def retrieve(self, request, pk):
        row = Book.objects.get(pk=pk)
        row = transform_signal(row)
        return Response(row)

    def destroy(self, request, pk):
        row = Book.objects.get(pk=pk)
        row.delete()
        return Response("Book deleted successfully")

def transform_signal(instance):
    data_dict = {}
    data_dict['id'] = instance.id
    data_dict["title"] = instance.title
    data_dict["author"] = instance.author
    data_dict["price"] = instance.price
    return data_dict

def map_book_object(data):
    return map(transform_signal, data)