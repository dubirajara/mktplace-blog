# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20170918_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.URLField(null=True, verbose_name='Image'),
        ),
    ]
