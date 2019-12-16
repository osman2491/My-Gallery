from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
    image = Image.img_details()
    return render(request,'welcome.html',{'image':image})

def display_photos(request):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()

    return render(request,'photos.html')

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})