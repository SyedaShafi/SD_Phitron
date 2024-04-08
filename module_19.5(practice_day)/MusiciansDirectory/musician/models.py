from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Violin', 'Violin'),
        ('Drums', 'Drums'),
        ('Flute', 'Flute'),
    ]
    instrument_type = models.CharField(max_length=40, choices=INSTRUMENT_CHOICES)
 
    def __str__(self):
        return self.first_name

