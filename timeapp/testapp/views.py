from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def times_view(request):
    time=datetime.datetime.now()
    s="The current date and time is: "+ str(time)
    return HttpResponse(s)
