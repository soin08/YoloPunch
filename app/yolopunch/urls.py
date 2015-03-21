from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from api.models import UserViewSet, ChallengeViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'punches', ChallengeViewSet)

urlpatterns = patterns('',
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^accounts/', include('registration.backends.default.urls')),
    url('^accounts/', include('registration.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('yolo.urls', namespace='yolo')),

)
