from django.conf.urls import patterns, url
from MyShop import views
from django.conf.urls.static import static
from Online_Shop import settings

__author__ = 'Anonymous'


urlpatterns= patterns('',
    url(r'^$', views.index,name="index"),
    url(r'^products/', views.products, name="products"),
)

