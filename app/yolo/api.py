from django.contrib.auth.models import User

from rest_framework import generics, permissions, viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .serializers import UserSerializer, ChallengeSerializer, PhotoSerializer
from .models import Challenge, Photo
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.Is, )



class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                      #IsAuthorOrReadOnly,
                                      )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class UserChallengeViewSet(viewsets.ModelViewSet):
    #queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                      IsAuthorOrReadOnly, )

    def get_queryset(self):
        queryset = super(UserChallengeViewSet, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ChallengePhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(ChallengePhotoViewSet, self).get_queryset()
        return queryset.filter(challenge__pk=self.kwargs.get('pk'))
