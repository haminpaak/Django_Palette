# Generated by Django 2.0.13 on 2020-11-09 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_exhibition_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibition',
            name='photo',
        ),
    ]
