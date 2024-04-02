from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    INSTRUMENT_CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Violin', 'Violin'),
        ('Drums', 'Drums'),
        ('Flute', 'Flute'),
    ]
    instrument_type = models.CharField(max_length=20, choices=INSTRUMENT_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"