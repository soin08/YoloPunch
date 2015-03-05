from django.conf.urls import patterns, include, url
from django.contrib import admin

from yolopunch import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^search/$', views.search, name='top'),
    url(r'^top/$', views.top, name='top' ),
    url(r'^top/(?P<filter>[users|punches])/$', views.top, name='top'),
    url(r'^(?P<username>[a-z0-9.-_]{3, 20})/$', views.user, name='user'),
    url(r'^(?P<username>[a-z0-9.-_]{3, 20})/punches/(?P<filter>[created|completed])/$',
         views.punches, name='punches'),
    url(r'^styleguide$', views.styleguide, name='styleguide'),

    # Examples:
    # url(r'^$', 'yolopunch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url( r'^$', views.index, name='index'),

    #url(r'^admin/', include(admin.site.urls)),
)
