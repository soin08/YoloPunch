from django.contrib.auth.models import User

from rest_framework import serializers

from yolo.models import Challenge, Photo, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfile
        fields = ('points', 'twitter', 'facebook', )


class UserSerializer(serializers.ModelSerializer):

    profile=UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  'profile')


class ChallengeSerializer(serializers.ModelSerializer):

    author = UserSerializer(
                            read_only=True,
                            required=False,
                    )
    recipients = UserSerializer(many=True)

    class Meta:
        model = Challenge
        #read_only_fields = ('pub_date', 'author', )


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

class Meta:
    model = Photo





