from django.conf.urls.defaults import patterns, include, url
#from django.conf.urls import *
#from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jjshop.views.home'),
    #url(r'^jjshop/', include('jjshop.jjshop.urls')),
    #url(r'^$','jjshop.catalogo.views.catalogo', name='catalogo'),
    url(r'^catalogo/$','jjshop.views.catalogo'),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/(.*)',admin.site.root),
)
