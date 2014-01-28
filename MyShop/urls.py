from django.conf.urls import patterns, url
from MyShop import views
from django.conf.urls.static import static
from Online_Shop import settings

__author__ = 'Anonymous'


urlpatterns= patterns('',
    url(r'^$', views.index,name="index"),
    url(r'^product/', views.product, name="product"),
    url(r'^section/', views.section, name="section"),
    url(r'^subSection/', views.subSection, name="subSection"),
    url(r'^writeComment/', views.writeComment, name="writeComment"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^login/', views.login, name="login"),
)

