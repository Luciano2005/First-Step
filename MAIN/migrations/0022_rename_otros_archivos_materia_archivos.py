# Generated by Django 4.1.2 on 2022-11-02 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0021_materia_imagen_materia_otros_archivos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materia',
            old_name='otros_archivos',
            new_name='archivos',
        ),
    ]