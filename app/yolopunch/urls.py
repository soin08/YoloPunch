from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^api/v1/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^accounts/', include('registration.backends.default.urls')),
    url('^accounts/', include('registration.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('yolo.urls', namespace='yolo')),

)
