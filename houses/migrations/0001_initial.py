# Generated by Django 3.0.7 on 2021-07-21 16:49

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_title', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('Novaya_settlement', models.CharField(blank=True, max_length=255)),
                ('hall', models.CharField(blank=True, max_length=255)),
                ('square_metres', models.CharField(max_length=255)),
                ('floors', models.CharField(blank=True, max_length=100)),
                ('bedroom', models.CharField(blank=True, max_length=100)),
                ('bedroom_1', models.CharField(blank=True, max_length=100)),
                ('bedroom_2', models.CharField(blank=True, max_length=100)),
                ('bedroom_3', models.CharField(blank=True, max_length=100)),
                ('bedroom_4', models.CharField(blank=True, max_length=100)),
                ('nursery', models.CharField(blank=True, max_length=100)),
                ('nursery_1', models.CharField(blank=True, max_length=100)),
                ('nursery_2', models.CharField(blank=True, max_length=100)),
                ('Kitchen', models.CharField(blank=True, max_length=100)),
                ('living_room', models.CharField(blank=True, max_length=100)),
                ('C_A', models.CharField(blank=True, max_length=100)),
                ('boiler_room', models.CharField(blank=True, max_length=100)),
                ('corridor', models.CharField(blank=True, max_length=100)),
                ('garage', models.CharField(blank=True, max_length=100)),
                ('Vestibule', models.CharField(blank=True, max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('house_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('house_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('house_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('house_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('house_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('house_photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_finished', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
