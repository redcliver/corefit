# Generated by Django 2.0.7 on 2018-07-16 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
        ('agenda', '0001_initial'),
        ('outro', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='prof1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outro.professor'),
        ),
    ]
