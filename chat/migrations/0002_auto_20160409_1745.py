# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-09 17:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='joinerID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='joinerID', to=settings.AUTH_USER_MODEL),
        ),
    ]
