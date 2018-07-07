# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-07 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_auto_20180706_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='long_short',
            field=models.CharField(choices=[('LONG', 'LONG'), ('SHORT', 'SHORT')], default='LONG', max_length=5),
            preserve_default=False,
        ),
    ]
