from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my Gallery')

def pictures(request):
    date = dt.date.today()
    return render(request, 'all-photos/pics.html', {"date": date,})