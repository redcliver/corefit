# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-16 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teste',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('imagem', models.ImageField(blank=True, upload_to=b'teste')),
            ],
        ),
    ]
