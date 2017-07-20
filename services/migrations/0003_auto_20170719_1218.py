# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-19 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20170718_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.CharField(blank=True, default='/company/send-email/', max_length=30, verbose_name='\u0421\u0421\u042b\u041b\u041a\u0410 \u041d\u0410 \u041e\u0422\u041f\u0420\u0410\u0412\u041a\u0423 \u0417\u0410\u042f\u0412\u041a\u0418 \u041d\u0410 \u0423\u0421\u041b\u0423\u0413\u0423'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=80, unique=True, verbose_name='\u041a\u0410\u041a\u0423\u042e \u0423\u0421\u041b\u0423\u0413\u0423 \u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c?'),
        ),
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(blank=True, default=None, max_length=2000, null=True, unique=True, verbose_name='\u0422\u0415\u041a\u0421\u0422 \u0414\u041b\u042f \u0421\u0422\u0420\u0410\u041d\u0418\u0426\u042b \u0423\u0421\u041b\u0423\u0413\u0418'),
        ),
    ]