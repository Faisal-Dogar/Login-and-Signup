from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home_page(request):
    return render(request, 'home.html')

def signup_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
       

        if pass1 != pass2:
            return HttpResponse("Confirm Password Not Match")
        else:
             emp = User.objects.create_user(name, email,pass1)
             emp.save()
             return redirect('login')
        
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        name1 = request.POST.get('username')
        pass1 = request.POST.get('pass')
        use = authenticate(request, username= name1, password=pass1)
        if use is not None:
            login(request,use)
            return redirect('home')
        else:
            return HttpResponse("Username or Password incorrect")

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

