# Generated by Django 4.1.3 on 2022-12-09 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0004_studio_images_delete_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]