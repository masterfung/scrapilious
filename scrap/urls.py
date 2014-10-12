from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^aptlogin/', include(admin.site.urls)),
    url(r'^$', 'apartment.views.home', name='home'),
    url(r'^listings/$', 'apartment.views.listings', name='listings'),
    url(r'^about/$', 'apartment.views.about', name='about'),
    url(r'^contact/$', 'apartment.views.contact', name='contact'),
    url(r'^graphs/$', 'apartment.views.graphs', name='graphs'),

    url(r'^login/$', 'apartment.views.login', name='login'),
)
