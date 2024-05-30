from django.shortcuts import redirect, render
from app.model.pages.employee import Employee

def EmpUser(request):
    data = Employee.objects.all()
    return render(request,'pages/Employee/employee.html', {'data': data})

def AddEmployee(request):
    if(request.method=="GET"):
        return render(request,'pages/Employee/addemployee.html')
    else:
        e_name = request.POST["Name"]
        e_location = request.POST["Location"]
        e_email = request.POST["Email"]

        try:
            employee = Employee.objects.get(e_name=e_name)
        except:
            employee = Employee(e_name=e_name, e_location=e_location,e_email=e_email)
            employee.save()
            return redirect(EmpUser)
        return render(request,'pages/Employee/addemployee.html')
        

def DeleteEmployee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect(EmpUser)

def UpdateEmployee(request,id):
    if request.method == "GET":
        employee = Employee.objects.get(id=id)
        return render(request,'pages/Employee/updateemployee.html', {'employee':employee})
    else:
        e_name = request.POST["Name"]
        e_location = request.POST["Location"]
        e_email = request.POST["Email"]

        employee = Employee(
            id = id,
            e_name = e_name,
            e_location = e_location,
            e_email = e_email,
        )
        employee.save()
        return redirect(EmpUser)


