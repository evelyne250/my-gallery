from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my Gallery')

def pictures(request):
    date = dt.date.today()
    return render(request, 'all-photos/pics.html', {"date": date,})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"categories": searched_category})

    else:
        message = "You haven't searched for anything"
        return render(request, 'all-photos/search.html',{"message":message})