from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, get_list_or_404, resolve_url
from django.http import HttpResponseRedirect, Http404

from rest_framework import viewsets, mixins, status, generics
#from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer

from rest_condition import And, Or

from .serializers import UserSerializer, UserProfileTrickySerializer, UserUpdateSerializer, ChallengeSerializer, PhotoSerializer

from yolopunch import settings
from yolo.models import Challenge, Photo, UserProfile

from .permissions import IsAuthor, IsSelf, IsReadOnly, IsPOST


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    """
    List view is forbidden.
    GET only for logged in users. (for everybody during development)
    POST, PATCH, DELETE - only for self.
    """
    permission_classes = (Or(IsSelf, IsReadOnly), )

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            #fields are not required or not blank
            return UserUpdateSerializer
        else:
            #fields are required
            return UserSerializer


class FollowsViewSet(viewsets.ViewSet):
    """
    Shows list of users that this user follows.
    Only currently logged-in user can edit his list.
    """
    permission_classes = (Or(IsSelf, IsReadOnly), )

    def list(self, request, user_username=None):
        """
        List follows
        """
        user = get_object_or_404(User, username=user_username)
        self.check_object_permissions(request, obj=user)
        follows_profiles = user.profile.follows
        serializer = UserProfileTrickySerializer(follows_profiles, many=True)
        #serializer.is_valid()
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
    permission_classes = (IsReadOnly, )

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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



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


class LoginView(APIView):
    renderer_classes = (TemplateHTMLRenderer, BrowsableAPIRenderer, JSONRenderer)

    def get(self, request, format="html"):
        if format == 'html':
            login_form = AuthenticationForm()
            return Response({'form':login_form},
                            template_name = 'registration/login.html')
        #for GET we only allow html renderer
        raise Http404()

    """
    Performs default auth behaviour
    """
    def post(self, request, format="html"):
        redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
        login_form = AuthenticationForm(request, data=request.data)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return HttpResponseRedirect(redirect_to)
        else:
            if format == 'html':
                return Response({'form':login_form},
                                template_name = 'registration/login.html')

            else:
                raise ValidationError(login_form.errors.as_json())
