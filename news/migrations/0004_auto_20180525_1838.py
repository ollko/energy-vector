# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2018-05-25 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180525_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['-timestamp', '-updated'], 'verbose_name': '\u041d\u043e\u0432\u043e\u0441\u0442\u043d\u0430\u044f \u0441\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u041d\u043e\u0432\u043e\u0441\u0442\u043d\u044b\u0435 \u0441\u0442\u0430\u0442\u044c\u0438'},
        ),
    ]