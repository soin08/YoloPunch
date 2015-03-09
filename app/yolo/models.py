from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from yolo import validators as v


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=20,
                                                      validators=[v.UsernameValidator()])
    points = models.IntegerField(default=5) #let's give 5 points for registration!
    followers = models.ManyToManyField("self", blank=True, null=True)


class YoloChallenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creator = models.OneToOneField(UserProfile, related_name='creator')
    recipients = models.ManyToManyField(UserProfile)
    pub_date = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateTimeField()
