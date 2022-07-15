from multiprocessing import context
from unicodedata import name
from django.shortcuts import redirect, render , HttpResponse
from .models import booking
from .forms import booking_form, contact_form

# Create your views here.
def index(request):
    return render(request, 'about_us.html')

def booking_options(request):
    return render(request, 'booking_options.html')

def table_booking(request):
    
    form = booking_form()
    
    if request.method == 'POST':
        form = booking_form(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {'form':form}
    return render(request, 'booking_form.html', context)

def update_booking(request):
    
    bookings = booking.objects.get(last_name="Bloggs")
    form = booking_form(instance=bookings)
        
    context = {'form':form}
    return render(request, 'booking_form.html', context)

def contact(request):
        form = contact_form()
    
        if request.method == 'POST':
            form = contact_form(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('index')
            
        context = {'form':form}
        return render(request, 'contact_form.html', context)