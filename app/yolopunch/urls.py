from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.views import LoginView

from rest_framework.urlpatterns import format_suffix_patterns

#our login should be able to render html or json, as requested
urlpatterns = patterns('',
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])

urlpatterns += patterns('',
    url(r'^api/v1/', include('api.urls', namespace='api')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url('^', include('yolo.urls', namespace='yolo')),
)
