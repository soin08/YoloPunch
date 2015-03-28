from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone

from datetime import timedelta

from rest_framework.parsers import JSONParser
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from yolo.models import Challenge, Photo, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Represents user profile.
    Points are updated automatically on events.
    Letting them being updated through the API is insecure.
    """
    class Meta:
        model=UserProfile
        fields = ('points', 'twitter', 'facebook', )
        read_only_fields = ('points', )


class UserSerializer(serializers.ModelSerializer):
    """
    Represents user.
    When creating a new user, we need to make sure that he provides
    at least username, first name, last name, email and password.
    """
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


class UserUpdateSerializer(UserSerializer):
    """
    When we update a user, none of the fields is required, but
    none of them can be blank.
    """
    username = serializers.CharField(
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


class UserProfileTrickySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model=UserProfile
        fields = ('user', )



class ChallengeSerializer(serializers.ModelSerializer):
    """
    Represents challenge
    """
    author = serializers.SlugRelatedField(
                                slug_field="username",
                                read_only=True,
                    )

    recipients = serializers.SlugRelatedField(
                              slug_field="username",
                              many=True,
                              queryset=User.objects.all()
                    )


    def validate_exp_date(self, value):
        """
        Make sure that exp_date is later then the current date by at least 5 minutes.
        pub_date is added automatically.
        """
        now = timezone.now()
        if now + timedelta(minutes=5) > value:
            raise serializers.ValidationError("minimum time interval between now and exp_date must be 5 minutes.")

        return value

    def validate_recipients(self, value):
        """
        Make sure that request.user is not in recipients
        """
        request = self.context.get("request")
        if request.user in value:
            raise serializers.ValidationError("author cannot be included to recipients")

        return value


    class Meta:
        model = Challenge
        read_only_fields = ('pub_date', )




"""
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





