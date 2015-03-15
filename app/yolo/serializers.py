from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Challenge, Photo


class UserSerializer(serializers.ModelSerializer):
    challenges = serializers.HyperlinkedIdentityField('challenges', view_name='userchallenge-list', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'challenges', )


class ChallengeSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    photos = serializers.HyperlinkedIdentityField('photos', view_name='challengephoto-list')

    def get_validation_exclusions(self):
        exclusions = super(ChallengeSerializer, self).get_validation_exclusions()
        return exclusions + ['author']

    class Meta:
        model = Photo





