# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 05:49
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('event_pic_url', models.ImageField(blank=True, null=True, upload_to=b'photos/%Y/%m/%d')),
                ('description', models.TextField(default=b'Please add a description')),
                ('event_type', models.CharField(choices=[(b'Movie', b'Movie'), (b'Concert', b'Concert'), (b'Conference', b'Conference'), (b'Festival', b'Festival'), (b'Wedding', b'Wedding'), (b'Party', b'Party')], max_length=100)),
                ('invite_only', models.BooleanField(default=False)),
                ('free', models.BooleanField(default=True)),
                ('age_restriction', models.BooleanField(default=False)),
                ('ticket_price', models.FloatField(blank=True, max_length=4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=254)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Venue'),
        ),
    ]