import requests
from django.shortcuts import redirect, render


def get_book_data(request):
    api_url = "http://127.0.0.1:8000/api/book/list/"
    response = requests.get(api_url)
    api_data = response.json()
    return render(request, 'api_pages/book_api.html', {'api_data': api_data})

def post_book_data(request):
    api_url = "http://127.0.0.1:8000/api/book/list/"
    api_data = {
        "title": request.POST['title'],
        "author": request.POST['author'],
        "price": request.POST['price']
    }
    response = requests.post(api_url, data=api_data)
    api_data = response.json()
    return redirect('book_api_data')
    # return render(request, 'api_pages/book_api.html', {'api_data': api_data})

def update_book_data(request, id):
    api_url = f"http://127.0.0.1:8000/api/book/{id}/"
    api_data = {
        "title": request.POST['title'],
        "author": request.POST['author'],
        "price": request.POST['price']
    }
    response = requests.put(api_url, data=api_data)
    api_data = response.json()
    return redirect('book_api_data')
    # return render(request, 'api_pages/book_api.html', {'api_data': api_data})

def delete_book_data(request, id):
    api_url = f"http://127.0.0.1:8000/api/book/{id}/"
    response = requests.delete(api_url)
    api_data = response.json()
    return redirect('book_api_data')
    # return render(request, 'api_pages/book_api.html', {'api_data': api_data})