from logging import PlaceHolder
from django.db import models
from phone_field import PhoneField
from django.utils import timezone


# Create your models here.

class booking(models.Model, PhoneField):
    booking_date = models.DateTimeField(default=timezone.now)
    number_of_guests = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    special_request = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-booking_date']
        
    def __str__(self):
        return self.id
    


