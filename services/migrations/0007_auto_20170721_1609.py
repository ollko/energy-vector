# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-21 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20170721_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.CharField(blank=True, choices=[(1, '/call_order/'), (2, '/maintenance_order/')], max_length=30, verbose_name='\u0421\u0421\u042b\u041b\u041a\u0410 \u041d\u0410 \u041e\u0422\u041f\u0420\u0410\u0412\u041a\u0423 \u0417\u0410\u042f\u0412\u041a\u0418 \u041d\u0410 \u0423\u0421\u041b\u0423\u0413\u0423'),
        ),
    ]
