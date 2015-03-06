# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YoloChallenge',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YoloUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator(message='Username is not valid', regex='^[a-z0-9.-_]{3,20}$')], max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='yolochallenge',
            name='creator',
            field=models.OneToOneField(to='yolo.YoloUser', related_name='creator'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='yolochallenge',
            name='recipients',
            field=models.ManyToManyField(to='yolo.YoloUser'),
            preserve_default=True,
        ),
    ]
