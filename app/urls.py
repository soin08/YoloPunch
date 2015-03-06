from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url('^', include('yolo.urls', namespace='yolo')),

    #url(r'^admin/', include(admin.site.urls)),
)
