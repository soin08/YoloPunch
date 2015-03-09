# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0004_auto_20150308_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(to='yolo.UserProfile', null=True, blank=True, related_name='followers_rel_+'),
            preserve_default=True,
        ),
    ]
