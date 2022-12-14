# Generated by Django 4.1.2 on 2022-10-23 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ESTUDIO', '0020_alter_respuestascerradas_respuesta_cerrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestascerradas',
            name='apropiacion',
        ),
        migrations.RemoveField(
            model_name='respuestascerradas',
            name='name',
        ),
        migrations.RemoveField(
            model_name='respuestascerradas',
            name='seccion',
        ),
        migrations.RemoveField(
            model_name='respuestascerradas',
            name='ultima_vez',
        ),
        migrations.AddField(
            model_name='respuestascerradas',
            name='pregunta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ESTUDIO.pregunta'),
        ),
        migrations.AlterField(
            model_name='respuestascerradas',
            name='respuesta_cerrada',
            field=models.CharField(max_length=30),
        ),
    ]
