# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-25 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='ok', max_length=250)),
                ('password', models.CharField(default='k', max_length=50)),
                ('code1', models.CharField(max_length=250, null=True)),
                ('code2', models.CharField(max_length=250, null=True)),
                ('code3', models.CharField(max_length=250, null=True)),
                ('code4', models.CharField(max_length=250, null=True)),
                ('code5', models.CharField(max_length=250, null=True)),
                ('code6', models.CharField(max_length=250, null=True)),
                ('status', models.IntegerField(default=1)),
                ('filled', models.BooleanField(default=False)),
            ],
        ),
    ]
