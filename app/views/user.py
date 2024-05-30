from django.shortcuts import redirect, render
from app.model.pages.user import Person
# import requests
from django.contrib import messages

# # for getting api data to frontend
# def User(request):
    # response = requests.get('http://127.0.0.1:8000/api/user/list/').json()
    # return render(request,'pages/User/user.html', {'response': response})

# # def AddPerson(request):
# #     response = requests.post('http://127.0.0.1:8000/api/user/list/').json()
# #     return render(request,'pages/User/adduser.html', {'response': response})

# # def delete(request,id):
# #     response = requests.delete('http://127.0.0.1:8000/api/user/<int:pk>/').json()
# #     return render(request,'pages/User/user.html', {'response': response})

# # def update(request,id):
# #     response = requests.put('http://127.0.0.1:8000/api/user/<int:pk>/').json()
# #     return render(request,'pages/User/user.html', {'response': response})


# # *************************



def User(request):
    persondata = Person.objects.all()
    return render(request,'pages/User/user.html', {'persondata': persondata})

def AddPerson(request):
    if(request.method=="GET"):
        return render(request,'pages/User/user.html')
    else:
       u_name = request.POST["Name"]
       u_location = request.POST["Location"]
       u_email = request.POST["Email"]

    try:
        person = Person.objects.get(u_name=u_name)
    except:
        person = Person(u_name=u_name, u_location=u_location,u_email=u_email)
        person.save()
        return redirect(User)
    return render(request,'pages/User/add.html')
        

def Delete(request,id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(User)

def Update(request,id):
    if request.method == "GET":
        person = Person.objects.get(id=id)
        return render(request,'pages/User/update.html', {'person':person})
    else:
        u_name = request.POST["Name"]
        u_location = request.POST["Location"]
        u_email = request.POST["Email"]

        person = Person(
            id=id,
            u_name = u_name,
            u_location = u_location,
            u_email = u_email,
        )
        person.save()
        return redirect(User)


def message_update(request):
    if AddPerson == True:
        messages.success(request, 'User Updated Successfully!!!')
    else:
        messages.warning(request, 'User Not added!!!')

        return redirect(User)
    return redirect(User)

