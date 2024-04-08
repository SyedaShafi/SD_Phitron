from django.db import models
from musician.models import MusicianModel
# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=100)

    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE, related_name='albums')

    album_release_date = models.DateField(auto_now = True)

    RATING_VAL = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
    ]

    rating = models.IntegerField(choices=RATING_VAL, default = 1)

    def __str__(self):
        return self.album_name