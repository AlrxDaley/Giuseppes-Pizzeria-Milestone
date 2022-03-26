from multiprocessing import context
from django.shortcuts import redirect, render , HttpResponse
from .models import booking
from .forms import booking_form

# Create your views here.
def index(request):
    return render(request, 'about_us.html')


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
    
    form = booking_form()
        
    context = {'form':form}
    return render(request, 'booking_form.html', context)