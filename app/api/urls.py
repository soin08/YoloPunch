from django.conf.urls import patterns, include, url

from rest_framework_nested import routers

from .views import UserViewSet, ChallengeViewSet, FollowerViewSet, FollowsViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'punches', ChallengeViewSet, base_name='challenge')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'followers', FollowerViewSet, base_name='follower')
users_router.register(r'follows', FollowsViewSet, base_name='follows')


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(users_router.urls)),
)

