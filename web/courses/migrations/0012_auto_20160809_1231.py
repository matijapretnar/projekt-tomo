# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-09 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20160420_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentenrollment',
            options={'ordering': ['user', 'course']},
        ),
        migrations.AlterField(
            model_name='problemset',
            name='solution_visibility',
            field=models.CharField(choices=[('H', 'Official solutions are hidden'), ('S', 'Official solutions are visible when solved'), ('V', 'Official solutions are visible')], default='S', max_length=20, verbose_name='Solution visibility'),
        ),
    ]
