# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-23 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformModel',
            fields=[
                ('resource_id', models.TextField(auto_created=True, max_length=32, unique=True)),
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('platform_type', models.CharField(choices=[('onem2m', 'OneM2M'), ('openhab', 'OpenHAB')], default='onem2m', max_length=32)),
                ('description', models.TextField(max_length=32, null=True)),
                ('namespace', models.CharField(choices=[('kube-system', 'Kube System')], default='kube-system', max_length=32)),
                ('label', models.TextField(max_length=32, null=True)),
                ('version', models.TextField(default='v1', max_length=32)),
            ],
            options={
                'db_table': 'platform',
            },
        ),
    ]
