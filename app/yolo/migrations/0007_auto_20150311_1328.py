# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0006_remove_userprofile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(default='', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(default='', null=True, blank=True),
            preserve_default=True,
        ),
    ]
