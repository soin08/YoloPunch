from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url('^accounts/', include('registration.backends.default.urls')),
    url('^accounts/', include('registration.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('yolo.urls', namespace='yolo')),

)
