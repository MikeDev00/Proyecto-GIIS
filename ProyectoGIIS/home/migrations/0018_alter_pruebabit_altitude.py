# Generated by Django 4.1 on 2022-09-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_pruebabit_altitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebabit',
            name='altitude',
            field=models.FloatField(blank=True, default=0, max_length=100, verbose_name='Altitud'),
        ),
    ]
