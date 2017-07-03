# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-02 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Callorderuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u0418\u041c\u042f')),
                ('text', models.CharField(max_length=200, verbose_name='\u0412\u041e\u041f\u0420\u041e\u0421')),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.ImageField(upload_to='certificates', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 .jpg \u0438\u043b\u0438 .jpeg')),
                ('certificate_1x', models.ImageField(default=None, null=True, upload_to='certificates')),
                ('certificate_2x', models.ImageField(default=None, null=True, upload_to='certificates')),
            ],
        ),
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Otziv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otziv', models.ImageField(help_text='PDF \u043d\u0435 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u0442\u0441\u044f!', upload_to='otziv')),
                ('otziv_1x', models.ImageField(default=None, null=True, upload_to='otziv')),
                ('otziv_2x', models.ImageField(default=None, null=True, upload_to='otziv')),
                ('text', models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='\u041d\u0410\u0411\u0415\u0420\u0418\u0422\u0415 \u041a\u0420\u0410\u0422\u041a\u041e \u0422\u0415\u041a\u0421\u0422 \u041e\u0422\u0417\u042b\u0412\u0410')),
            ],
        ),
    ]
