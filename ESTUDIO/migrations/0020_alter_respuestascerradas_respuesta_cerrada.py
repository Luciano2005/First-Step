# Generated by Django 4.1.2 on 2022-10-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESTUDIO', '0019_remove_respuestascerradas_pregunta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestascerradas',
            name='respuesta_cerrada',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]