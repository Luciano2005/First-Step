# Generated by Django 4.1.2 on 2022-11-01 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0018_tarea_realizado_alter_tarea_prioridad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='realizado',
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.CharField(choices=[('Bajo', 'Bajo'), ('Medio', 'Medio'), ('Alto', 'Alto')], default='Bajo', max_length=20),
        ),
    ]