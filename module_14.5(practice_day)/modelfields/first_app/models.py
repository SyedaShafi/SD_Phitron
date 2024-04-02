from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    date_field = models.DateField( default = datetime.datetime.now)
  

