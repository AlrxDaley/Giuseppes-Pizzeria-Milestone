
from django.db import models
from django.utils import timezone


# Create your models here.

class booking(models.Model):
    order_id= models.CharField(max_length=120, blank= True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    booking_date = models.DateField(default=timezone.now, max_length=255)
    booking_ToD = models.TimeField(default=timezone.now, max_length=255)
    number_of_guests = models.IntegerField()
    phone_number = models.CharField(max_length=1024)
    special_request = models.TextField(blank=True, max_length=1024)
    
    class Meta:
        ordering = ['-order_id']
        
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
    


