from django.conf.urls import patterns, include, url
from django.contrib import admin

from yolo import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^top/$', views.top_all, name='top_all' ),
    url(r'^top/users/$', views.top_users, name='top_users'),
    url(r'^top/punches/$', views.top_challenges, name='top_challenges'),
    url(r'^(?P<username>[a-z0-9.-_]{1,30})/following/$', views.following, name='following'),
    url(r'^(?P<username>[a-z0-9.-_]{1,30})/followers/$', views.followers, name='followers'),
    url(r'^(?P<username>[a-z0-9.-_]{1,30})/punches/$',
         views.challanges_all, name='challenges_all'),
    url(r'^(?P<username>[a-z0-9.-_]{1,30})/punches/created/$',
         views.challanges_created, name='challenges_created'),
    url(r'^(?P<username>[a-z0-9.-_]{1,30})/punches/completed/$',
         views.challanges_completed, name='challenges_competed'),
    url(r'^(?P<username>[a-z0-9.-_]{1,30})/$', views.user, name='user'),
    url(r'^styleguide$', views.styleguide, name='styleguide'),

    # Examples:
    # url(r'^$', 'yolopunch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url( r'^$', views.index, name='index'),

    #url(r'^admin/', include(admin.site.urls)),
)
