# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-26 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='profissional',
        ),
    ]
