# Generated by Django 2.2 on 2021-07-08 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marketprice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoniamarketprice',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finlandmarketprice',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
