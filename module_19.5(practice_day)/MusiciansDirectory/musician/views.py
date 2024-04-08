from django.shortcuts import render, redirect
from . forms import MusicianForm
from . models import MusicianModel
from django.contrib import messages
# Create your views here.
def add_musician(request):
    if not request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Musician added')
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm()
        
    return render(request, 'add_musician.html', {'form': form})


def musician_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('homepage')

    musician = MusicianModel.objects.get(pk = id)
    form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            messages.success(request, 'Musician edited Successfully')
            form.save()
            return redirect('homepage')
            
    return render(request, 'add_musician.html', {'form': form})

