from django.shortcuts import render

from django.http import HttpResponse

def index(request) :
    # toabout = "Link to " + '<a href="/rango/about/">About</a>'
    # return HttpResponse("Rango says hey there partner!" + " " + toabout)

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request) :
    # toindex = "Link to " + '<a href="/rango/">Index</a>'
    # return HttpResponse("Rango says here is the about page." + " " + toindex)

    context_dict = {'boldmessage': 'This tutorial has been put together by Ben Maguire'}
    return render(request, 'rango/about.html', context=context_dict)
