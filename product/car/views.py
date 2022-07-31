from django.shortcuts import render
from . import models

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    spec1 = models.Specification()
    spec1.name = "Rangerover SV"
    spec1.price = 5000000
    spec1.images2 = 'car1.jpg'
    spec1.desc = "Pixel LED headlights with signature DRL"
    
    spec2 = models.Specification()
    spec2.name = "Rangerover SE"
    spec2.price = 5000000
    spec2.images2 = 'car2.jpg'
    spec2.desc = "Cabin lighting Three-zone Climate Control"
    
    spec3 = models.Specification()
    spec3.name = "Rangerover HSE"
    spec3.price = 5000000
    spec3.images2 = 'car3.jpg'
    spec3.desc = "Pivi Pro with 33.27 cm (13.1) Touchscreen Wireless Apple CarPlay1 and Wireless Android Auto"
    
    spec4 = models.Specification()
    spec4.name = "Landrover"
    spec4.price = 5000000
    spec4.images2 = 'car4.jpg'
    spec4.desc = "An exquisite interpretation of Range Rover Luxury and Personalisation"
    
    specs = [spec1,spec2,spec3,spec4]
    return render(request,'index.html',{'specs':specs,})

