# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-16 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plano',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('periodo', models.CharField(choices=[(b'1', b'Avulsa'), (b'2', b'Mensal'), (b'2', b'Trimestral')], max_length=1)),
            ],
        ),
    ]
