from django.shortcuts import render, redirect
from album.models import AlbumModel
from . forms import RegintrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def home(request):
    data = AlbumModel.objects.all()
    return render(request, 'home.html', {'data': data})


def signup(request):
    if request.method == "POST":
        form = RegintrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            return redirect('login')
    else:
        form = RegintrationForm()

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = name, password = user_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successful')
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})



def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('homepage')

    messages.warning(request, 'User logged out.')
    logout(request)
    return redirect('login')