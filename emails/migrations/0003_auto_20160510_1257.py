# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20160510_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsource',
            name='specificData',
            field=models.TextField(default='defaultna hodnota'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailsource',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
