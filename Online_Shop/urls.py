from django.conf.urls import patterns, include, url

from django.contrib import admin
from Online_Shop import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Online_Shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^MyShop/', include('MyShop.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
