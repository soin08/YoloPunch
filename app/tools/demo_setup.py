import os, sys

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yolopunch.settings")

import django
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone

import datetime

from random import randint

from yolo.models import Challenge

def create_demo_users(num):
    counter = User.objects.count()
    print(counter)
    for i in range(num):
        counter += 1
        user = User.objects.create_user('demouser%s' % counter,
                                                        'demouser%s@example.com' % counter,
                                                        '12345')

def create_demo_challenges(user, recipients, num):
    counter = user.challenges.count()
    for i in range(num):
        counter += 1
        punch = Challenge()
        punch.title = "Demo punch %s" % counter
        punch.description = "This is a demo punch. There is nothing n\
                                        more to say about it, really."
        punch.author = user
        punch.pub_date = timezone.now()
        punch.exp_date = timezone.now() + datetime.timedelta(days=2)
        punch.save()
        punch.recipients = recipients

        punch.save()
        print('challenge %s creaded for user %s' % (str(counter),
                user.username))


NUM_USERS = 7
create_demo_users(NUM_USERS)
print("created %s new users" % NUM_USERS)

NUM_USERS_FOR_PUNCHES = 3
NUM_PUNCHES = 5
NUM_RECIPIENTS = 3

for i in range(NUM_USERS_FOR_PUNCHES):
    user = User.objects.get(pk=i+1)
    recipients = []
    for j in range(NUM_RECIPIENTS):
        recipients.append(User.objects.get(pk=i+1+j+1))
    create_demo_challenges(user, recipients, NUM_PUNCHES)


#counter = User.objects.count()
#print(counter)
"""
i=0

user = User.objects.create_user('demouser%s' % i,
                                                        'demouser%s@example.com' % i,
                                                        '12345')
"""
