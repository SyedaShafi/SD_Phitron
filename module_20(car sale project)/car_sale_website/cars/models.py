from django.db import models
from brands.models import BrandModel
from django.contrib.auth.models import User
# Create your models here.

class CarModel(models.Model):
    car_name = models.CharField(max_length=100)
    car_price = models.IntegerField()
    car_brand_name = models.ForeignKey(BrandModel,on_delete = models.CASCADE) 
    car_details = models.TextField()
    car_quantity = models.IntegerField()
    car_image = models.ImageField(upload_to='media/uploads/', blank = True, null = True)

    def buy_car(self):
        if self.car_quantity > 0:
            self.car_quantity -= 1
            self.save()
            return True
        return False

    def __str__(self):
        return self.car_name


class CommentModel(models.Model):
    comment = models.ForeignKey(CarModel, on_delete = models.CASCADE, related_name='comment')
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"comments by {self.name}"
    

class PurchaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} purchased {self.car.car_name}"
