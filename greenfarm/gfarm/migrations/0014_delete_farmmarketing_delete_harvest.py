# Generated by Django 4.2.5 on 2023-09-26 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gfarm', '0013_remove_farmmarketing_maize_remove_harvest_maize_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FarmMarketing',
        ),
        migrations.DeleteModel(
            name='Harvest',
        ),
    ]
