# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-16 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='hora',
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
