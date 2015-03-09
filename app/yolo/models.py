from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save

from yolo import validators as v


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=5) #let's give 5 points for registration!
    followers = models.ManyToManyField("self", blank=True, null=True)


 # This function will create a UserProfile whenever a User is created
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)



class YoloChallenge(models.Model):
    title = models.CharField(max_length=100)# This function will create a UserProfile whenever a User is created
    description = models.CharField(max_length=500)
    creator = models.OneToOneField(UserProfile, related_name='creator')
    recipients = models.ManyToManyField(UserProfile)
    pub_date = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateTimeField()
