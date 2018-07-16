# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-16 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('outro', '0001_initial'),
        ('plano', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('data_nasc', models.DateField(blank=True, default=False, null=True)),
                ('data_venc', models.DateField(blank=True, default=False, null=True)),
                ('queixa', models.CharField(blank=True, max_length=500, null=True)),
                ('objetivo', models.CharField(blank=True, max_length=500, null=True)),
                ('ativo', models.CharField(choices=[(b'1', b'Sim'), (b'2', b'Nao')], max_length=1)),
                ('plan1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.plano')),
                ('prof1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outro.professor')),
            ],
        ),
        migrations.CreateModel(
            name='pagamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_pag', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
