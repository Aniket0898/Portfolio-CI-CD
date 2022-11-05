from django.shortcuts import render
from .models import images

# Create your views here.

def index(request):

    images1 = images()
    images1.img1 = 'aniket_profile.jpg'
    images1.img2 = 'mainfile.jpg'
    images1.img3 = 'myfavicon.png'
    images1.img4 = 'new-apple-touch-icon.png'

    return render(request, "index.html", {'images1': images1})
