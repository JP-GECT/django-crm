from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    #check to see if loged in
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        # authenticate user
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request,user)
            messages.success(request,('You have been logged in'))
            return redirect('home')
        else:
            messages.success(request,('Error logging in - Please try again'))
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out...'))
    return redirect('home')