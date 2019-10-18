# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-10-16 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=264)),
                ('LastName', models.CharField(max_length=264)),
                ('Email', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]