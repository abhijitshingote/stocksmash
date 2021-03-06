# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyprice', models.DecimalField(decimal_places=2, max_digits=9)),
                ('buytimestamp', models.DateField(auto_now=True)),
                ('targetprice', models.DecimalField(decimal_places=2, max_digits=9)),
                ('tradeenddate', models.DateField()),
                ('stoplossprice', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('tickersymbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock')),
            ],
        ),
    ]
