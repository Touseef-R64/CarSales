from django.db import models
import uuid
from django.utils import timezone
# Create your models here.


class Vehicle(models.Model):
    transmission_CHOICES = [
        ('automatic', 'Automatic transmission'),
        ('manual', 'Manual Transmission'),]
    STEERING_CHOICES = [
        ('left', 'american cars'),
        ('right', 'normal cars'),]
    FUEL_CHOICES = [
        ('diesel', 'diesel oil'),
        ('petrol', 'petrol oil'),]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    name = models.CharField(max_length=200)
    model_code = models.CharField(max_length=50)
    ref_num = models.CharField(max_length=50)
    chasis = models.CharField(max_length=50)
    engine_size = models.IntegerField(null=True,blank=True)
    mileage = models.IntegerField(null=True,blank=True)
    engine_code = models.CharField(max_length=10,null=True,blank=True)

    location = models.CharField(max_length=50,null=True,blank=True)
    version = models.CharField(max_length=100,null=True,blank=True)
    transmission = models.CharField(max_length=10, choices=transmission_CHOICES,null=True,blank=True)
    steering = models.CharField(max_length=10, choices=STEERING_CHOICES,null=True,blank=True)
    fuel = models.CharField(max_length=10, choices=FUEL_CHOICES,null=True,blank=True)
    ext_color = models.CharField(max_length=20,null=True,blank=True)
    seats = models.IntegerField(default=4)
    doors = models.IntegerField(default=4)
    m3 = models.FloatField(null=True,blank=True)
    dimension_height = models.FloatField(null=True,blank=True)
    dimension_width = models.FloatField(null=True,blank=True)
    dimension_lenght = models.FloatField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    max_cap = models.FloatField(null=True,blank=True)


    registration_date = models.DateField(null=True, blank=True)
    manufacture_date = models.DateField(null=True, blank=True)
    price = models.PositiveBigIntegerField(default=0)

    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)