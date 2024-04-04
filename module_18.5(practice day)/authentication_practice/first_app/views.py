from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
# Create your views here.

def home(request):
    return render(request, 'home.html')



def user_register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            form.save()
            return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, 'signup_page.html', {'form': form})





def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)

        if form.is_valid():
            name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username =name, password = user_password)

            if user is not None:
                messages.success(request, 'Logged In Successfully')
                login(request, user)
                return redirect('profile')
               
            else:
                messages.warning(request, 'No such user available!')
                return redirect('user_register')
    else:
        form = AuthenticationForm()

    return render(request, 'login_page.html', {'form': form})




def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('user_register')






def user_logout(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Logged Out Successfully')
        logout(request)
        return redirect('homepage') 
    else:
        return redirect('user_register')






def password_change(request):

    if not request.user.is_authenticated:
        return redirect('user_register')
    
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            messages.warning(request, 'Password Changed Successfully')
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
        
    else:
        form = PasswordChangeForm(user = request.user)

    return render(request, 'password_change.html', {'form': form})






def set_password(request):

    if not request.user.is_authenticated:
        return redirect('user_register')
    
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            messages.warning(request, 'Password Set Successful')
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    
    else:
        form = SetPasswordForm(user = request.user)
    
    return render(request, 'set_password.html', {'form': form})

