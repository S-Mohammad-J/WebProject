import os
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from MyShop.models import SlideshowProduct


def index(request):
    #return HttpResponse("Hello World, I'm here")
    slideshowProducts = SlideshowProduct.objects.all()
    context={"slideshowProducts":slideshowProducts}
    return render(request,"Home.html",context)

