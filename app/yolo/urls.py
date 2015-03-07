from django.conf.urls import patterns, include, url
from django.contrib import admin

from yolo import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='top'),
    url(r'^top/$', views.top, name='top' ),
    url(r'^top/(?P<filter>[users|punches])/$', views.top, name='top'),
    url(r'^(?P<username>[a-z0-9.-_]{3,20})/$', views.user, name='user'),
    url(r'^(?P<username>[a-z0-9.-_]{3,20})/following/$', views.following, name='following'),
    url(r'^(?P<username>[a-z0-9.-_]{3,20})/followers/$', views.followers, name='followers'),
    url(r'^(?P<username>[a-z0-9.-_]{3,20})/punches/$',
         views.punches, name='challanges'),
    url(r'^(?P<username>[a-z0-9.-_]{3,20})/punches/(?P<filter>[created|completed])/$',
         views.punches, name='challanges'),
    url(r'^styleguide$', views.styleguide, name='styleguide'),

    # Examples:
    # url(r'^$', 'yolopunch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url( r'^$', views.index, name='index'),

    #url(r'^admin/', include(admin.site.urls)),
)
