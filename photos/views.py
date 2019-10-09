from django.shortcuts import render
import datetime as dt
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my Gallery')

def pictures(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)