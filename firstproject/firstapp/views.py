from django.shortcuts import render
from django.http import HttpResponse

import datetime



def display(request):
    return HttpResponse("<h1>My first django app</h1>")



def home(request):
    return render(request,'firstapp/firstApp.html')


def displayDateTime(request):

    dt = datetime.datetime.now()
    s = "<b>Date and Time :</b>" +str(dt)
    return HttpResponse(s)
# Create your views here.
