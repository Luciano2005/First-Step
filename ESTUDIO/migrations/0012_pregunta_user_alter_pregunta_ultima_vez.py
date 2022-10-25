# Generated by Django 4.0.5 on 2022-10-19 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ESTUDIO', '0011_alter_pregunta_apropiacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='ultima_vez',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]