# Generated by Django 4.1.2 on 2022-10-22 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ESTUDIO', '0016_remove_respuestascerradas_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='respuesta_cerrada',
        ),
        migrations.AddField(
            model_name='respuestascerradas',
            name='pregunta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ESTUDIO.pregunta'),
        ),
        migrations.AddField(
            model_name='respuestascerradas',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
