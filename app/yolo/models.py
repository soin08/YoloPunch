from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    points = models.IntegerField(default=5) #let's give 5 points for registration!
    followers = models.ManyToManyField('self', symmetrical=False)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


 # This function will create a UserProfile whenever a User is created
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Challenge(models.Model):
    title = models.CharField(max_length=100)#
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User, related_name='challenges')
    recipients = models.ManyToManyField(UserProfile)
    pub_date = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateTimeField()

class Photo(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")
