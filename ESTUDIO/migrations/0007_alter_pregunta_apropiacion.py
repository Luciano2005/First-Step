# Generated by Django 4.0.5 on 2022-10-11 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESTUDIO', '0006_alter_pregunta_apropiacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='apropiacion',
            field=models.IntegerField(blank=True, choices=[(1, 'Otra Vez'), (2, 'Dificil'), (3, 'Bien'), (4, 'Facil')]),
        ),
    ]
