from django.shortcuts import render
from . forms import contactForm
# Create your views here.
def home(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'first_app/home.html', {'form': form})
