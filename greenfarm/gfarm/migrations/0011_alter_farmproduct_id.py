# Generated by Django 4.2.5 on 2023-09-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfarm', '0010_alter_farmproduct_maize_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmproduct',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]