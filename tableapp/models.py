
from django.db import models
from phone_field import PhoneField
from django.utils import timezone
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker



# Create your models here.

class booking(models.Model):
    order_id= models.CharField(max_length=120, blank= True)
    booking_date = models.DateTimeField(default=timezone.now, max_length=255)
    booking_time = models.DateTimeField(default=timezone.now, max_length=255)
    number_of_guests = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
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
    


