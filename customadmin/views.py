from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, 'account not found')
                return HttpResponseRedirect(request.Meta.get('HTTP_REFERER'))
            
            user_obj = authenticate(username=username,password=password)

            if user_obj is user_obj.is_superuser:
                login(request, user_obj)
                return redirect('/dashboard/')
            
            messages.info(request, 'Invalid username or password')
            return redirect('/')

        return render(request, 'login.html')
    
    except Exception as e:
        print(e)

def dashboard(request):
    return render(request, 'dashboard.html')