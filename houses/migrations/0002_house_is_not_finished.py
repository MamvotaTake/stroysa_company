# Generated by Django 3.0.7 on 2021-07-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='is_not_finished',
            field=models.BooleanField(default=False),
        ),
    ]
