import requests
from django.shortcuts import redirect, render

def get_employee_data(request):
    api_url = "http://127.0.0.1:8000/api/employee/list/"
    response = requests.get(api_url)
    api_data = response.json()
    return render(request, 'api_pages/employee_api.html', {'api_data': api_data})

def post_employee_data(request):
    api_url = "http://127.0.0.1:8000/api/employee/list/"
    api_data = {
        "e_name": request.POST['e_name'],
        "e_location": request.POST['e_location'],
        "e_email": request.POST['e_email']
    }
    response = requests.post(api_url, data=api_data)
    api_data = response.json()
    return redirect("employee_api_data")
    # return render(request, 'api_pages/employee_api.html', {'api_data': api_data})

def update_employee_data(request, id):
    api_url = f"http://127.0.0.1:8000/api/employee/{id}/"
    api_data = {
        "e_name": request.POST['e_name'],
        "e_location": request.POST['e_location'],
        "e_email": request.POST['e_email']
    }
    response = requests.put(api_url, data=api_data)
    api_data = response.json()
    return redirect("employee_api_data")
    # return render(request, 'api_pages/employee_api.html', {'api_data': api_data})

def delete_employee_data(request,id):
    api_url = f"http://127.0.0.1:8000/api/employee/{id}/"
    response = requests.delete(api_url)
    api_data = response.json()
    return redirect("employee_api_data")
    # return render(request, 'api_pages/employee_api.html', {'api_data': api_data})