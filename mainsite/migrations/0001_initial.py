# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-11 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('section_name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('last_updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
