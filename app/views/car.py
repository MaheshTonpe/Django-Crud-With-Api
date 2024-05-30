from django.shortcuts import redirect, render
from app.model.pages.car import Car

def CarObject(request):
    data = Car.objects.all()
    return render(request,'pages/Car/car.html', {'data': data})

def AddCar(request):
    if(request.method=="GET"):
        return render(request,'pages/Car/addcar.html')
    else:
        brand_name = request.POST["Brand Name"]
        model_name = request.POST["Model Name"]
        price = request.POST["Price"]

        try:
            car = Car.objects.get(brand_name=brand_name)
        except:
            car = Car(brand_name=brand_name, model_name=model_name,price=price)
            car.save()
            return redirect(CarObject)
        return render(request,'pages/Car/addcar.html')
        

def DeleteCar(request,id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect(CarObject)

def UpdateCar(request,id):
    if request.method == "GET":
        car = Car.objects.get(id=id)
        return render(request,'pages/Car/updatecar.html',{'car':car})
    else:
        brand_name = request.POST["Brand Name"]
        model_name = request.POST["Model Name"]
        price = request.POST["Price"]

        car = Car(
            id = id,
            brand_name = brand_name,
            model_name = model_name,
            price = price,
        )
        car.save()
        return redirect(CarObject)


