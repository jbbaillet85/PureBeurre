from collections import UserList
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .form import RegisterForm, LoginForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        email= request.POST.get('email')
        print(email)
        password= request.POST.get('password')
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('spaceUser')
        if form.is_valid():
            return render(request, 'spaceUser.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def spaceUser(request):
    return render(request, 'spaceUser.html')