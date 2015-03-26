from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated

from rest_condition import And, Or

from .serializers import UserSerializer, UserProfileTrickySerializer, UserUpdateSerializer, ChallengeSerializer, PhotoSerializer

from yolo.models import Challenge, Photo, UserProfile

from .permissions import IsAuthor, IsSelf, IsReadOnly


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, Or(IsSelf, IsReadOnly), )

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            #fields are not required but not blank
            return UserUpdateSerializer
        else:
            #fields are required
            return UserSerializer


class FollowsViewSet(viewsets.ViewSet):
    """
    Shows list of users that requested user follows.
    Only currently logged-in user can edit this list.
    """
    permission_classes = (IsAuthenticated, Or(IsSelf, IsReadOnly), )

    def list(self, request, user_username=None):
        """
        List follows
        """
        user = get_object_or_404(User, username=user_username)
        self.check_object_permissions(request, obj=user)
        follows_profiles = user.profile.follows
        serializer = UserProfileTrickySerializer(follows_profiles, many=True)
        return Response(serializer.data)

    def create(self, request, user_username):
        """
        Add to follows
        """
        username = request.data.get("username", None)
        if username:
            if user_username == username:
                raise ValidationError({"detail" : "Users cannot follow themselves."})
            user = get_object_or_404(User, username=user_username)
            self.check_object_permissions(request, obj=user)
            new_followed_user = get_object_or_404(User, username=username)
            user.profile.follows.add(new_followed_user.profile)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError({"username": ["This field is required." ]})

    def destroy(self,request, user_username, pk):
        """
        Remove from follows
        """
        user = get_object_or_404(User, username=user_username)
        self.check_object_permissions(request, obj=user)
        followed_user = get_object_or_404(User, username=pk)
        user.profile.follows.remove(followed_user.profile)
        return Response(status=status.HTTP_204_NO_CONTENT)


class FollowerViewSet(viewsets.ViewSet):
    """
    Shows read-only list of users who follow requested user.
    """
    permission_classes = (IsAuthenticated, Or(IsSelf, IsReadOnly), )

    def list(self, request, user_username=None):
        """
        List follows
        """
        user = get_object_or_404(User, username=user_username)
        self.check_object_permissions(request, obj=user)
        followers_profiles = user.profile.followers
        serializer = UserProfileTrickySerializer(followers_profiles, many=True)
        return Response(serializer.data)



class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (IsAuthenticated, Or(IsAuthor, IsReadOnly),  )
    #def get_queryset(self):
        #user = self.request.user
        #return Challenge.objects.filter(author=user)



class UserChallengeViewSet(viewsets.ModelViewSet):
    #queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (IsAuthenticated, Or(IsAuthor, IsReadOnly), )

    def get_queryset(self):
        queryset = super(UserChallengeViewSet, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated, )


class ChallengePhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        queryset = super(ChallengePhotoViewSet, self).get_queryset()
        return queryset.filter(challenge__pk=self.kwargs.get('pk'))


# Create your views here.
