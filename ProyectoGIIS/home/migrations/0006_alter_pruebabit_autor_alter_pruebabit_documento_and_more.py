# Generated by Django 4.1 on 2022-09-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_pruebabit_autor_pruebabit_documento_pruebabit_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebabit',
            name='autor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pruebabit',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='bitacoras/'),
        ),
        migrations.AlterField(
            model_name='pruebabit',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
