# Generated by Django 4.2.16 on 2024-11-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_buyer_age_buyer_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='hashed_password',
            field=models.CharField(default='', max_length=100000),
        ),
    ]