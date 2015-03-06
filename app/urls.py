from django.conf.urls import patterns, include, url
from django.contrib import admin

from yolopunch import views

urlpatterns = patterns('',
    url(r'^styleguide$', views.styleguide, name='styleguide'),
    url('^$', include('yolo.urls'), namespace='yolo'),

    #url(r'^admin/', include(admin.site.urls)),
)
