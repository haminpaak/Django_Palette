# Generated by Django 2.0.13 on 2020-11-09 15:53

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20201110_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='test'),
        ),
    ]
