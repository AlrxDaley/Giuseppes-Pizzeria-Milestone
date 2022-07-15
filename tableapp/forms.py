from django.forms import ModelForm
from .models import booking, contact

class booking_form(ModelForm):
    
    class Meta:
        model = booking
        fields = '__all__'
        
class contact_form(ModelForm):
    
    class Meta:
        model = contact
        fields = '__all__'
