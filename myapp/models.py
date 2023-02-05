from django.db import models

#class Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vehicles(models.Model):
    brand=models.CharField(max_length=255)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="vehicle")   
      
