from django.contrib.auth.models import User

from rest_framework import generics, permissions


from .serializers import UserSerializer, ChallengeSerializer#, PhotoSerializer
from .models import Challenge, Photo
from .permissions import PostAuthorCanEditPermission


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'


class ChallengeMixin(object):
    model = Challenge
    serializer_class = ChallengeSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]

    def pre_save(self, obj):
        """Force author to the current user on save"""
        obj.author = self.request.user
        return super(ChallengeMixin, self).pre_save(obj)


class ChallengeList(ChallengeMixin, generics.ListCreateAPIView):
    pass


class ChallengeDetail(ChallengeMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserChallengeList(generics.ListAPIView):
    model = Challenge
    serializer_class = ChallengeSerializer

    def get_queryset(self):
        queryset = super(UserChallengeList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class PhotoList(generics.ListCreateAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Photo
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PostPhotoList(generics.ListAPIView):
    model = Photo
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(PostPhotoList, self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))

