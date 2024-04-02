from django.shortcuts import render
from musician.models import MusicianModel
from album.models import AlbumModel
def home(request):
    album = AlbumModel.objects.all()
    return render(request, 'home.html', {'album': album})