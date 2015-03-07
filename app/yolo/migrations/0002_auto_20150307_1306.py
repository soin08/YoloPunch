# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import yolo.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yolo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(validators=[yolo.validators.UsernameValidator()], max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='yolochallenge',
            name='creator',
            field=models.OneToOneField(related_name='creator', to='yolo.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='yolochallenge',
            name='recipients',
            field=models.ManyToManyField(to='yolo.UserProfile'),
            preserve_default=True,
        ),
    ]
