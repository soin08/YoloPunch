from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import permissions, viewsets, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


from .serializers import UserSerializer, UserProfileTrickySerializer, UserUpdateSerializer, ChallengeSerializer, PhotoSerializer
from yolo.models import Challenge, Photo, UserProfile
from .permissions import IsAuthorOrReadOnly, IsSelfOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    #serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticated,
                                           #IsSelfOrReadOnly, )

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return UserUpdateSerializer
        else:
            return UserSerializer

class FollowerFollowingViewSet(viewsets.ViewSet):
    def get_related_profile_list(self, user):
        pass

    def add_profile_to_related_list(self, user, related_profile):
        pass

    def list(self, request, user_username=None):
        user = get_object_or_404(User, username=user_username)
        related_profiles = self.get_related_profile_list(user)
        serializer = UserProfileTrickySerializer(related_profiles, many=True)

        return Response(serializer.data)

    def create(self, request, user_username):
        username = request.data.get("username")
        if username:
            if user_username == username:
                raise ValidationError({"detail" : "Users cannot follow themselves."})

            user = get_object_or_404(User, username=user_username)
            new_related_user = get_object_or_404(User, username=username)
            #user.profile.followers.add(new_follower.profile)
            self.add_profile_to_related_list(user, new_related_user.profile)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError({"username": ["This field is required." ]})

    """-
    def retrieve(self, request, user_username, pk):
        follower = get_object_or_404(User, username=pk)
        #make sure that the requested follower actually follows the user
        get_list_or_404(follower.profile.follows, user__username=user_username)
        serializer = UserSerializer(follower)
        return Response(serializer.data)
    """

    def destroy(self,request, user_username, pk):
         user = get_object_or_404(User, username=user_username)
         follower = get_object_or_404(User, username=pk)
         user.profile.followers.remove(follower.profile)
         return Response(status=status.HTTP_204_NO_CONTENT)


class FollowerViewSet(FollowerFollowingViewSet):
    def get_related_profile_list(self, user):
        return user.profile.followers

    def add_profile_to_related_list(self, user, related_profile):
        user.profile.followers.add(related_profile)


class FollowsViewSet(FollowerFollowingViewSet):
    def get_related_profile_list(self, user):
        return user.profile.follows

    def add_profile_to_related_list(self, user, related_profile):
        user.profile.follows.add(related_profile)



class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (permissions.IsAuthenticated,
                                           IsAuthorOrReadOnly,  )
    #def get_queryset(self):
        #user = self.request.user
        #return Challenge.objects.filter(author=user)



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


# Create your views here.
