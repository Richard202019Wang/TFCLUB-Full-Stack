# Generated by Django 4.1.3 on 2022-12-10 01:40

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='posts/default.jpg', null=True, upload_to=accounts.models.upload_to),
        ),
    ]
