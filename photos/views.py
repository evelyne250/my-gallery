from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse
from .models import Image,Category,Location

# Create your views here.
def pictures(request):
   
    images = Image.pictures()
    return render(request, 'all-photos/pics.html',{'images':images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"categories": searched_category})

    else:
        message = "You haven't searched for anything"
        return render(request, 'all-photos/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})