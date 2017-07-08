# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-08 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20170708_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genset',
            name='prime_kva',
            field=models.DecimalField(decimal_places=1, max_digits=8, verbose_name='PRP(Prime)/\u043a\u0412\u0410'),
        ),
        migrations.AlterField(
            model_name='genset',
            name='prime_kw',
            field=models.DecimalField(decimal_places=1, max_digits=8, verbose_name='PRP(Prime)/\u043a\u0412\u0442'),
        ),
        migrations.AlterField(
            model_name='genset',
            name='stand_by_kva',
            field=models.DecimalField(decimal_places=1, max_digits=8, verbose_name='ESP(Stand-by)/\u043a\u0412\u0410'),
        ),
        migrations.AlterField(
            model_name='genset',
            name='stand_by_kw',
            field=models.DecimalField(decimal_places=1, max_digits=8, verbose_name='ESP(Stand-by)/\u043a\u0412\u0442'),
        ),
    ]
