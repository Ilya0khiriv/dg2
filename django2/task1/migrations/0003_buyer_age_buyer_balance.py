# Generated by Django 4.2.16 on 2024-11-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_game_cost_game_description_game_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
