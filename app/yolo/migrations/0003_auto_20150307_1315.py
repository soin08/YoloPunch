# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0002_auto_20150307_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yolouser',
            name='user',
        ),
        migrations.DeleteModel(
            name='YoloUser',
        ),
    ]
