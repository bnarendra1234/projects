# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_od',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=30)),
                ('odpurpose', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('no_of_days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fdp_attended_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=30)),
                ('attended_on_topic', models.CharField(max_length=100)),
                ('resource_person', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('no_of_days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fdp_conduct_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('fdp_topic', models.CharField(max_length=100)),
                ('resource_person', models.CharField(max_length=100)),
                ('pno', models.IntegerField()),
                ('venue', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('no_of_faculty_participated', models.IntegerField()),
                ('no_of_days', models.IntegerField()),
            ],
        ),
    ]
