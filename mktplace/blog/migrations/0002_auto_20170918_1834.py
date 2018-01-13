# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 16:34
from __future__ import unicode_literals

import tagulous.models.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagulous_Post_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count',
                 models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected',
                 models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='tagulous_post_tags',
            unique_together=set([('slug',)]),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, force_lowercase=True,
                                                  help_text='Enter a comma-separated tag string', max_count=5,
                                                  to='blog.Tagulous_Post_tags'),
        ),
    ]
