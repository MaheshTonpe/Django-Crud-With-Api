from django.shortcuts import redirect, render
from app.model.pages.bike import Bike

def BikeObject(request):
    data = Bike.objects.all()
    return render(request,'pages/Bike/bike.html', {'data': data})

def AddBike(request):
    if(request.method=="GET"):
        return render(request,'pages/Bike/addBike.html')
    else:
        brand_name = request.POST["Brand Name"]
        model_name = request.POST["Model Name"]
        price = request.POST["Price"]

        try:
            obj = Bike.objects.get(brand_name=brand_name)
        except:
            obj = Bike(brand_name=brand_name, model_name=model_name,price=price)
            obj.save()
            return redirect(BikeObject)
        return render(request,'pages/Bike/addbike.html')
        

def DeleteBike(request,id):
    obj = Bike.objects.get(id=id)
    obj.delete()
    return redirect(BikeObject)

def UpdateBike(request,id):
    if request.method == "GET":
        obj = Bike.objects.get(id=id)
        return render(request,'pages/Bike/updatebike.html',{'obj':obj})
    else:
        brand_name = request.POST["Brand Name"]
        model_name = request.POST["Model Name"]
        price = request.POST["Price"]

        obj = Bike(
            id = id,
            brand_name = brand_name,
            model_name = model_name,
            price = price,
        )
        obj.save()
        return redirect(BikeObject)


