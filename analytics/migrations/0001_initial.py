# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('listing_number', models.IntegerField(null=True)),
                ('listing_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
