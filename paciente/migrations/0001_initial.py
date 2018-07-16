# Generated by Django 2.0.7 on 2018-07-16 17:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plano', '0001_initial'),
        ('outro', '__first__'),
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
                ('ativo', models.CharField(choices=[('1', 'Sim'), ('2', 'Nao')], max_length=1)),
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
