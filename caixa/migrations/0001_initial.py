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
            name='caixa_geral',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[(b'1', b'Entrada'), (b'2', b'Saida')], max_length=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desc', models.CharField(max_length=200)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
