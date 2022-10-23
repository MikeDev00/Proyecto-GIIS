# Generated by Django 4.1 on 2022-10-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_rename_prueba_blogpost_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pruebabit',
            name='temp',
        ),
        migrations.AddField(
            model_name='pruebabit',
            name='temperatura',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=8, null=True, verbose_name='Temperatura'),
        ),
        migrations.AlterField(
            model_name='pruebabit',
            name='altitud',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=8, null=True, verbose_name='Altitud'),
        ),
        migrations.AlterField(
            model_name='pruebabit',
            name='medición',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=8, null=True),
        ),
    ]
