from django.shortcuts import render

from django.http import HttpResponse

def index(request) :
    toabout = "Link to " + '<a href="/rango/about/">About</a>'
    
    return HttpResponse("Rango says hey there partner!" + " " + toabout)

def about(request) :
    toindex = "Link to " + '<a href="/rango/">Index</a>'
    return HttpResponse("Rango says here is the about page." + " " + toindex)
