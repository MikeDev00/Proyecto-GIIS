# Generated by Django 4.1 on 2022-10-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_pruebabit_altitude'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Graficos',
        ),
        migrations.DeleteModel(
            name='Infinitos',
        ),
        migrations.RemoveField(
            model_name='pruebabit',
            name='altitude',
        ),
        migrations.AddField(
            model_name='pruebabit',
            name='altitud',
            field=models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=8, null=True, verbose_name='Altitud'),
        ),
        migrations.AddField(
            model_name='pruebabit',
            name='medicion',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pruebabit',
            name='medtype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pruebabit',
            name='unidad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pruebabit',
            name='longitude',
            field=models.FloatField(blank=True, default=None, max_length=100, null=True, verbose_name='Longitud'),
        ),
    ]
