# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='td',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('pno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
