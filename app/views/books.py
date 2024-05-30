from django.shortcuts import redirect, render
from app.model.pages.books import Book

def BookObject(request):
    data = Book.objects.all()
    return render(request,'pages/Books/book.html', {'data': data})

def AddBook(request):
    if(request.method=="GET"):
        return render(request,'pages/Books/addbook.html')
    else:
        title = request.POST["Title"]
        author = request.POST["Author"]
        price = request.POST["Price"]

        try:
            obj = Book.objects.get(title=title)
        except:
            obj = Book(title=title, author=author,price=price)
            obj.save()
            return redirect(BookObject)
        return render(request,'pages/Books/addbook.html')
        

def DeleteBook(request,id):
    obj = Book.objects.get(id=id)
    obj.delete()
    return redirect(BookObject)

def UpdateBook(request,id):
    if request.method == "GET":
        obj = Book.objects.get(id=id)
        return render(request,'pages/Books/updatebook.html',{'obj':obj})
    else:
        title = request.POST["Title"]
        author = request.POST["Author"]
        price = request.POST["Price"]

        obj = Book(
            id = id,
            title = title,
            author = author,
            price = price,
        )
        obj.save()
        return redirect(BookObject)


