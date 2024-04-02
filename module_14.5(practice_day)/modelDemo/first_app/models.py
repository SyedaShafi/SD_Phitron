from django.db import models
import datetime
# Create your models here.
class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True, default=0)  

    date_field = models.DateField( default = datetime.datetime.now)

    date_time_field = models.DateTimeField(default = datetime.datetime.now )

    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    duration_field = models.DurationField(default=0)

   