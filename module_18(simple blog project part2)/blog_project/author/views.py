from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

from . import forms
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})


def user_login(request):

    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data = request.POST)

        if login_form.is_valid():
            name = login_form.cleaned_data['username']
            user_password = login_form.cleaned_data['password']
            user = authenticate(username = name, password = user_password)

            if user is not None:
                messages.success(request, 'Logged in successfully')
                login(request, user)
                return redirect('profile')
            
            else:
                messages.warning(request, 'No such user available!')
                return redirect('register')
    
    else:
        login_form = AuthenticationForm()

    return render(request, 'register.html', {'form': login_form, 'type':
                                             'Login'})


@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data': data})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeProfileData(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeProfileData(instance = request.user)
    
    return render(request, 'update_profile.html', {'form': profile_form})


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully.')
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'password_change.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')