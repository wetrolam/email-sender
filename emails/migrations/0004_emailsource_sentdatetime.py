# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0003_auto_20160510_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsource',
            name='sentDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
