import requests
from django.shortcuts import redirect, render

def get_api_data(request):
    api_url = "http://127.0.0.1:8000/api/user/list/"
    response = requests.get(api_url)
    api_data = response.json()
    return render(request, 'api_pages/user_api.html', {'api_data': api_data})

def post_api_data(request):
    api_url = "http://127.0.0.1:8000/api/user/list/"
    api_data = {
        "u_name": request.POST['u_name'],
        "u_location": request.POST['u_location'],
        "u_email": request.POST['u_email']
    }
    response = requests.post(api_url, data=api_data)
    api_data = response.json()
    return redirect("user_api_data")
    # return render(request, 'api_pages/user_api.html', {'api_data': api_data})

def delete_api_data(request, id):
    api_url = f"http://127.0.0.1:8000/api/user/{id}/"
    response = requests.delete(api_url)
    api_data = response.json()
    return redirect("user_api_data")
    # return render(request, 'api_pages/user_api.html', {'api_data': api_data})

def update_api_data(request, id):
    api_url = f"http://127.0.0.1:8000/api/user/{id}/"
    api_data = {
        "u_name": request.POST['u_name'],
        "u_location": request.POST['u_location'],
        "u_email": request.POST['u_email']
    }
    response = requests.put(api_url, data=api_data)
    api_data = response.json()
    return redirect("user_api_data")
    # return render(request, 'api_pages/user_api.html', {'api_data': api_data})

