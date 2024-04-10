from django.shortcuts import render, redirect
from brands.models import BrandModel
from cars.models import CarModel
from cars.forms import RegintrationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, update_session_auth_hash
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm

def home(request, id=None):
    data = BrandModel.objects.all()
    if id == None:
        cars = CarModel.objects.all()
    else:
        cars = CarModel.objects.filter(car_brand_name_id = id)
    print(cars)
    return render(request, 'home.html', {'data': data, 'cars': cars })


def register(request):
    if request.method == 'POST':
        register_form = RegintrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('user_login')
    else:
        register_form = RegintrationForm()
    
    return render(request, 'signup.html', {'form': register_form})


class UserLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged in information is not correct')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserLogoutView(View):
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('register')
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('homepage'))
        logout(request)
        return redirect(reverse_lazy('homepage'))
    
    




def password_change(request):

    if not request.user.is_authenticated:
        return redirect('register')
    
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
        return redirect('register')
    
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