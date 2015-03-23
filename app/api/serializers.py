from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.utils.six import BytesIO

from rest_framework.parsers import JSONParser
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from yolo.models import Challenge, Photo, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Points are updated automatically on events.
    Letting them being updated through the API is insecure.
    """
    class Meta:
        model=UserProfile
        fields = ('points', 'twitter', 'facebook', )
        read_only_fields = ('points', )

"""
When creating a new user, we need to make sure that he provides
at least username, first name, last name, email and password.
"""
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
                                     min_length=3,
                                     max_length=30,
                                     validators=[UniqueValidator(queryset=User.objects.all())],
                        )
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)
    profile=UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                       'email', 'password', 'profile')
        #read_only_fields = ('username', )

    def create(self, validated_data):
        #the profile property will be created automatically using signals
        return User.objects.create(**validated_data)

"""
However, when we update a user, none of the fields is required, but
none of them can be blank.
"""
class UserUpdateSerializer(UserSerializer):
    username = serializers.CharField(
                                     #read_only=True,
                                     required=False,
                                     min_length=3,
                                     max_length=30,
                                     validators=[UniqueValidator(queryset=User.objects.all())],
                        )
    first_name = serializers.CharField(max_length=100, required=False)
    last_name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(write_only=True, min_length=6, required=False)

    def update(self, instance, validated_data):

        profile_data = validated_data.pop('profile', None)

        if profile_data:
            profile = instance.profile
            profile.twitter = profile_data.get('twitter', profile.twitter)
            profile.facebook = profile_data.get('facebook', profile.facebook)
            profile.save()

        instance.username = validated_data.get('username', instance.username)
        #instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)
            # SEND EMAIL ABOUT PASSWORD CHANGE
        instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance

class UserTrickySerializer(serializers.ModelSerializer):
    pass

class UserProfileTrickySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model=UserProfile
        fields = ('user', )



class ChallengeSerializer(serializers.ModelSerializer):

    """
    author = serializers.SlugRelatedField(
                            #author will be set automatically to the current user
                            slug_field='username',
                            required=False,
                            read_only=True,
                    )
    """
    author = serializers.HyperlinkedRelatedField(
                            read_only=True,
                            #queryset=User.objects.all,
                            view_name='user-detail',
                            lookup_field='username'
                        )
    recipients = serializers.HyperlinkedRelatedField(
                            view_name='user-detail',
                            many=True,
                            #read_only=True,
                            lookup_field='username',
                            queryset=User.objects.all(),
                        )
    #recipients_write =

    class Meta:
        model = Challenge
        read_only_fields = ('pub_date', 'author', )

"""
   def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.first_name)
        instance.description = validated_data.get('description', instance.description)
        recipients_data = validated_data.get('recipients', None)
        if recipients_data:

"""

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

class Meta:
    model = Photo





