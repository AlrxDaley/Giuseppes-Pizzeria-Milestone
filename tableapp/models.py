from django.db import models
from phone_field import PhoneField

# Create your models here.

class booking(models.Model, PhoneField):
    booking_date = models.DateTimeField(auto_now=True)
    number_of_guests = models.IntegerField(default=0)
    first_name = models.CharField(max_length=50, min_length = 1)
    last_name = models.CharField(max_length=50, min_length = 1)
    phone_number = models.PhoneField(blank=True, help_text='Contact phone number')
    special_request = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.first_name