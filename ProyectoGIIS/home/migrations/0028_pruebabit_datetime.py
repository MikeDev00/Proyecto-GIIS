# Generated by Django 4.1 on 2022-10-11 20:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_remove_blogpost_content_remove_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruebabit',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]