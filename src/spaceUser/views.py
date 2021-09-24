from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import RegisterForm, LoginForm
from spaceUser.models import User

# Create your views here.
def register(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            last_name = User.objects.values("last_name")
            return HttpResponse(f"Vous êtes bien inscris {last_name}" )
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def identification(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password= request.POST.get('password')
        user1 = authenticate(request, username=username, password=password)
        if user1 is not None:
            login(request, user1)
            user_log = User.objects.get(username = user1)
            context = {"last_name" : user_log.last_name, "email": user_log.email }
            return render(request, 'spaceUser.html', context)
    else:
        messages.add_message(request, messages.INFO, "Utilisateur ou mot de passe incorrect")    
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def spaceUser(request):
    return render(request, 'spaceUser.html')