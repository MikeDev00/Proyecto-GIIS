# Generated by Django 4.1 on 2022-09-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_pruebabit_prueba"),
    ]

    operations = [
        migrations.AddField(
            model_name="graficos",
            name="nomx",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Nombre de Archivo"
            ),
        ),
        migrations.AddField(
            model_name="graficos",
            name="nomy",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Nombre de Archivo"
            ),
        ),
        migrations.AddField(
            model_name="graficos",
            name="nomz",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Nombre de Archivo"
            ),
        ),
    ]
