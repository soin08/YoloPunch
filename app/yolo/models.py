from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from yolo import validators

from django.core.validators import RegexValidator

class YoloUser(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=20,
                                                      validators=[ RegexValidator(
           regex='^[a-z0-9.-_]{3,20}$',
           message='Username is not valid',
    )])

    """
    RegexValidator(
           regex='^[a-z0-9.-_]{3,20}$',
           message = 'Username is not valid'
    )
"""

class YoloChallenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    creator = models.OneToOneField(YoloUser, related_name='creator')
    recipients = models.ManyToManyField(YoloUser)
    pub_date = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()
