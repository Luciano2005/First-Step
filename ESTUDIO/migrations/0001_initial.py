# Generated by Django 4.0.5 on 2022-10-10 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apropiacion', models.IntegerField(choices=[(1, 'Nombre1'), (2, 'Nombre2'), (3, 'Nombre3'), (4, 'Nombre4'), (5, 'Nombre5')])),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
