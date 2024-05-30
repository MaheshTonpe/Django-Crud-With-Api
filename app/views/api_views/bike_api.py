import requests
from django.shortcuts import redirect, render

def get_bike_data(request):
    api_url = "http://127.0.0.1:8000/api/bike/list/"
    response = requests.get(api_url)
    api_data = response.json()
    return render(request, 'api_pages/bike_api.html', {'api_data': api_data})

def post_bike_data(request):
    api_url = "http://127.0.0.1:8000/api/bike/list/"
    api_data = {
        "brand_name": request.POST['brand_name'],
        "model_name": request.POST['model_name'],
        "price": request.POST['price']
    }
    response = requests.post(api_url, data=api_data)
    api_data = response.json()
    return redirect("bike_api_data")
    # return render(request, 'api_pages/bike_api.html', {'api_data': api_data})

def update_bike_data(request, id):
    api_url = f"http://127.0.0.1:8000/api/bike/{id}/"
    api_data = {
        "brand_name": request.POST['brand_name'],
        "model_name": request.POST['model_name'],
        "price": request.POST['price']
    }
    response = requests.put(api_url, data=api_data)
    api_data = response.json()
    return redirect("bike_api_data")
    # return render(request, 'api_pages/bike_api.html', {'api_data': api_data})

def delete_bike_data(request, id):
    api_url = f"http://127.0.0.1:8000/api/bike/{id}/"
    response = requests.delete(api_url)
    api_data = response.json()
    return redirect("bike_api_data")
    # return render(request, 'api_pages/bike_api.html', {'api_data': api_data})