# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 05:58
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(max_length=40, null=True, srid=4326),
        ),
    ]
