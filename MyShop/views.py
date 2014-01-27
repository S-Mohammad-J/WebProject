import os
import random
from random import randint
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from MyShop.models import SlideshowProduct, Section, SubSection, Product


def index(request):
    #return HttpResponse("Hello World, I'm here")
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    Products=Product.objects.all()
    suggestProducts=[]
    portarafdars=[]
    for x in range(1,5):
        r = randint(1,Products.__len__())
        suggestProducts.append(Product.objects.get(id=r))
    for x in range(1,5):
        r = randint(1,Products.__len__())
        portarafdars.append(Product.objects.get(id=r))


    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections,
             "suggestProducts":suggestProducts,
             "portarafdars":portarafdars,
    }
    return render(request,"Home.html",context)

def product(request):
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }
    return render(request,"product.html",context)

def section(request):
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }
    return render(request,"section.html",context)

def subSection(request):
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }
    return render(request,"section.html",context)