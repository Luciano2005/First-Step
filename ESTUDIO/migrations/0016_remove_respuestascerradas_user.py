# Generated by Django 4.1.2 on 2022-10-22 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ESTUDIO', '0015_remove_respuestascerradas_pregunta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuestascerradas',
            name='user',
        ),
    ]
