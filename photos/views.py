from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse
from .models import Image,Category,Location
import pyperclip
# Create your views here.
def pictures(request):
   
    images = Image.objects.all()
    location = Location.objects.all()
    # image_found = Image.copy_image()
    # print(pyperclip.paste())
   
    return render(request, 'all-photos/pics.html',{'images':images,'location':location})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")

        searched_images = Image.search_by_category(search_term)
        print(searched_images)
        message = f"{search_term}"
        
        

        return render(request, 'all-photos/search.html',{"message":message,"searched_image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def filter_by_location(request, id):
    location = Location.objects.all()
    images = Image.objects.filter(location__id=id)
    
    return render(request, "all-photos/location.html",{'images':images,'location':location})