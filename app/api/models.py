from django.contrib.auth.models import User

from rest_framework import permissions, viewsets


from .serializers import UserSerializer, ChallengeSerializer, PhotoSerializer
from yolo.models import Challenge, Photo
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                      IsAuthorOrReadOnly, )



class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                      IsAuthorOrReadOnly,  )



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

