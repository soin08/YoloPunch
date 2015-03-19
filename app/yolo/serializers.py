from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Challenge, Photo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #punches = serializers.HyperlinkedIdentityField(
     #                       view_name='userchallenge-list',
                            #lookup_field='username'
      #              )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',  )


class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    #author = UserSerializer(required=False)
    author = serializers.HyperlinkedIdentityField(
                            view_name='user-list',
                 )
    #photos = serializers.HyperlinkedIdentityField(
    #                        view_name='challengephoto-list',
    #            )

    #def get_validation_exclusions(self):
    #   exclusions = super(ChallengeSerializer, self).get_validation_exclusions()
    #   return exclusions + ['author']

    class Meta:
        model = Challenge


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

class Meta:
    model = Photo





