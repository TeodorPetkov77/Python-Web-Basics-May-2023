# Generated by Django 4.2.2 on 2023-06-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0002_rename_car_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
