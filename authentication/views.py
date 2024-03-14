from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm,SignupForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user


# Create your views here.
@unauthenticated_user
def signup(request):
    
    if request.method == 'GET':
        form = SignupForm()
        return render(request,'auth/signup.html',{'form':form})
    
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            return  redirect('login')
        
        else:
            messages.warning(request, "The passowords must match and of 8 or more mixed characters without including your username.")
            return render(request,'auth/signup.html',{'form':form})
    
   
# login user

@unauthenticated_user
def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)


            if user is not None:

                auth.login(request, user)

                return redirect('home')
        else:
            messages.warning(request, "Username or password is incorrect")
            context = {'form':form}
            return render(request, 'auth/login.html', context=context)
                


    context = {'form':form}

    return render(request, 'auth/login.html', context=context)





# logout the user


def logout(request):
    auth.logout(request)
    
    return redirect('login')