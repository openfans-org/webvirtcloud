# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-24 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instances', '0003_instance_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]