# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-02 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170702_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genset',
            name='spec',
            field=models.FileField(blank=True, default=None, null=True, upload_to=b'', verbose_name='pdf \u0444\u0430\u0439\u043b \u0441\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
    ]
