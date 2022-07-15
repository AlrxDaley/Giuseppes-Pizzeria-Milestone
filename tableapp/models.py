
from pyexpat import model
from django.db import models
from phone_field import PhoneField
from django.utils import timezone



# Create your models here.

class booking(models.Model):
    order_id= models.CharField(max_length=120, blank= True)
    booking_date = models.DateField(default=timezone.now)
    booking_time = models.TimeField(default=timezone.now)
    number_of_guests = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    special_request = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-booking_date']
        
    def __str__(self):
        return self.first_name


class contact(models.Model):
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=256, blank=True)
    message = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-email']
    
    def __str__(self):
        return self.name
    


