from django.shortcuts import render, redirect
from . forms import AlbumForm
from . models import AlbumModel
from django.contrib import messages
# Create your views here.
def add_album(request):
    if not request.user.is_authenticated:
        return redirect('homepage')

    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Album added successfully')
            form.save()
            return redirect('homepage')
    else:
        form = AlbumForm()
        
    return render(request, 'add_album.html', {'form': form} )




def album_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('homepage')

    musician = AlbumModel.objects.get(pk = id)
    form = AlbumForm(instance=musician)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=musician)
        if form.is_valid():
            messages.success(request, 'Album edited Successfully')
            form.save()
            return redirect('homepage')
            
    return render(request, 'add_album.html', {'form': form})


def album_delete(request, id):
    if not request.user.is_authenticated:
        return redirect('homepage')

    album = AlbumModel.objects.get(pk=id)
    messages.warning(request, 'Album deleted successfully')
    album.delete()
    return redirect('homepage')