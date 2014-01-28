import os
import random
from random import randint
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
# Create your views here.
from MyShop.models import SlideshowProduct, Section, SubSection, Product, Comment, Customer


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
    productID=request.path_info.split("/")
    productID=productID[productID.__len__()-1]
    comments=Comment.objects.filter(product__id=int(productID))
    print("////////////sssss///////////////////")
    print(productID)
    print("///////////////////////////////")

    #product = SlideshowProduct.objects.all()
    #sections=Section.objects.all()
    #subSections=SubSection.objects.all()
    productObject=Product.objects.get(id=int(productID))
    context={"productObject":productObject,
             "comments":comments,
    }
    return render(request, "product.html",context)

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

def writeComment(request):
    #c = {}
    #c.update(csrf(request))
    print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    #if request.is_ajax():
    print("*********************")
    print(request.POST)
    print("*********************")
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }
    return render(request,"Home.html",context)

def signup(request):
    print("ooooooooooooooooooooooooooooooo")
    temp=dict(request.POST)
    print("3333333333ooo")
    print(str(temp).encode('utf-8'))
    if(temp):
        print("kjkj")
        empty=0
        for key in temp:
            if(str(temp[key])=="['']"):
                print("khalieeeee")
                empty=1
            else:
                print("ffff")
        if(empty==0):
            for key in temp:
                temp[key]=str(temp[key])[2:-2]
            customer=Customer(username=temp["rusername"],password=temp["rcpassword"],firstName=temp["rfirstName"],
            lastName=temp["rlastName"],address=temp["address"],tel=temp["phone"],email=temp["remail"])
            print(customer.username,"nnnnnnnnnnnnnnnnnnnnnn")
            customer.save()
            return HttpResponseRedirect("/MyShop/login")

    else:
        print("signup/ get")
    #t=request.POST

    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }

    return render(request,"signup.html",context)

def login(request):
    slideshowProducts = SlideshowProduct.objects.all()
    sections=Section.objects.all()
    subSections=SubSection.objects.all()
    context={"slideshowProducts":slideshowProducts,
             "sections":sections,
             "subSections":subSections
    }
    return render(request,"login.html",context)