# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2018-05-25 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=100, unique_for_date='publish', verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
