# Generated by Django 4.1 on 2022-10-21 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_alter_blogpost_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='prueba',
            new_name='content',
        ),
    ]
