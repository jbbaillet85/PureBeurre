from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import RegisterForm, LoginForm
from homepage.forms import SearchForm
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
            context = {}
            return render(request, 'spaceUser.html', context)
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
            form_search = SearchForm()
            context = {"last_name" : user_log.last_name, "email": user_log.email, 'form_search':form_search }
            return render(request, 'spaceUser.html', context)
    else:
        messages.add_message(request, messages.INFO, "Utilisateur ou mot de passe incorrect")    
    form = LoginForm()
    form_search = SearchForm()
    return render(request, 'login.html', {'form': form, 'form_search':form_search})

@login_required(login_url='login')
def spaceUser(request):
    form_search = SearchForm()
    user = User.objects.get(id=request.user.id)
    context = {'form_search':form_search, 'user': user}
    return render(request, 'spaceUser.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')