from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
    image = Image.img_details()
    return render(request,'welcome.html')

def display_photos(request):

    return render(request,'photos.html')