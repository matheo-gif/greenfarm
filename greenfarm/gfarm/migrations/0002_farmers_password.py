# Generated by Django 4.2.5 on 2023-09-15 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gfarm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmers',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]