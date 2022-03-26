from django.forms import ModelForm
from .models import booking

class booking_form(ModelForm):
    
    class Meta:
        model = booking
        fields = '__all__'
