import os
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from MyShop.models import SlideshowProduct, Section, SubSection


def index(request):
    #return HttpResponse("Hello World, I'm here")
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }
    return render(request,"Home.html",context)

def products(request):
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }
    return render(request,"product.html",context)