# Generated by Django 4.1 on 2022-10-11 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0026_rename_prueba2_comment_prueba"),
    ]

    operations = [
        migrations.RemoveField(model_name="blogpost", name="content",),
        migrations.RemoveField(model_name="comment", name="content",),
    ]
