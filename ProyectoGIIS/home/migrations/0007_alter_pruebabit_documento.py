# Generated by Django 4.1 on 2022-09-09 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_pruebabit_autor_alter_pruebabit_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebabit',
            name='documento',
            field=models.FileField(blank=True, null=True, upload_to='bitacora/'),
        ),
    ]