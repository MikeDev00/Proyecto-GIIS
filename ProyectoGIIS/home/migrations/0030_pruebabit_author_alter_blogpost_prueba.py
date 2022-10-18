# Generated by Django 4.1 on 2022-10-13 12:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0029_rename_datetime_pruebabit_datenow"),
    ]

    operations = [
        migrations.AddField(
            model_name="pruebabit",
            name="author",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="prueba",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Contenido"
            ),
        ),
    ]