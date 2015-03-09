# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0003_auto_20150307_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yolochallenge',
            old_name='expires',
            new_name='exp_date',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
