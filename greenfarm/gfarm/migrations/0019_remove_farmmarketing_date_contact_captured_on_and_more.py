# Generated by Django 4.2.5 on 2023-10-07 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfarm', '0018_alter_farmmarketing_date_alter_farmproduct_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmmarketing',
            name='date',
        ),
        migrations.AddField(
            model_name='contact',
            name='captured_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='farmmarketing',
            name='traded_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
