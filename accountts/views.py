from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
#from django.contrib.auth.models import auth
from .forms import RegistrationForm
def registration(request):
    if request.method =='POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = RegistrationForm()
    context={
        'form':form

    }
    return render(request,'registration.html',context)





# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['my_key'] = 'my_value'
            my = request.session.get('my_key')
            print(my)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method ==  'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:   
            if  User.objects.filter(email=email).exists():
                print('The email already registered') 
                messages.info(request, 'The email already registered')  
                return redirect('register')
            else:
                u1= User.objects.create_user(username=username,email=email,
                                            password=password1,first_name=first_name,
                                            last_name=last_name)
                u1.save()
                print("success......................")
                return redirect('login')
        else:
            print("Passowrd does not mmatch")
            messages.info(request, "Password does not match") 
            return redirect('register') 
        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')






