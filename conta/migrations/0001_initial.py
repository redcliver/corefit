# Generated by Django 2.0.7 on 2018-07-16 17:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('data_reg', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_venc', models.DateTimeField()),
                ('data_pag', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('1', 'Em Aberto'), ('2', 'Paga')], max_length=1)),
            ],
        ),
    ]
