from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse
from .models import Image,Category,Location

# Create your views here.
def pictures(request):
   
    images = Image.pictures()
    return render(request, 'all-photos/pics.html',{'images':images})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")

        searched_images = Image.search_by_category(search_term)
        print(searched_images)
        message = f"{search_term}"
        
        

        return render(request, 'all-photos/search.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
