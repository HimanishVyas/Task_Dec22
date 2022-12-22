from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Product
# Create your views here.


def home(request):
    return render(request, 'home.html')

def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
     
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username = username, email = email,
                 password = pass1,first_name = fname, last_name = lname)
        

        myuser.save()

        messages.success(request, 'Your acount hse been created')

        # return redirect('signin')
        return HttpResponse("Congo u have Created your Account Successfuly")
       
    
    return render(request, 'signUp.html')

def signin(request):
    
    if request.method == "POST":
            uname = request.POST['uname']
            # print(email)
            password = request.POST['pass1']
           
            user = authenticate(request ,username = uname, password = password)
            
            
            if user is not None:
            
                login(request, user)
                print(request.user.id)
                fname = user.first_name
                print(fname)
                return render(request, 'product.html', {'fname' : fname})
                
            else:
                messages.error(request, "invalid")
    

    return render(request, 'signin.html')

def cart(request):
    return render(request, 'cartScreen.html')
    