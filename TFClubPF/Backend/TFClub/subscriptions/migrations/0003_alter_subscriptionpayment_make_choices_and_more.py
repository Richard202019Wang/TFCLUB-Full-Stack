# Generated by Django 4.1.3 on 2022-11-19 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_alter_subscriptionpayment_make_choices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionpayment',
            name='make_choices',
            field=models.CharField(choices=[('1', 'payment is made immediately after subscription.'), ('2', 'each upcoming payment will be automatically made in the beginning of their period.')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='make_choices',
            field=models.CharField(choices=[('1', 'payment is made immediately after subscription.'), ('2', 'each upcoming payment will be automatically made in the beginning of their period.')], max_length=1),
        ),
    ]
