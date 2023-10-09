# Generated by Django 4.2.5 on 2023-09-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfarm', '0007_remove_harvest_maize_delete_farmmarketing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('Central', 'Central Region'), ('Coast', 'Coast Region'), ('Eastern', 'Eastern Region'), ('Nairobi', 'Nairobi Region'), ('North Eastern', 'North Eastern Region'), ('Nyanza', 'Nyanza Region'), ('Rift Valley', 'Rift Valley Region'), ('Western', 'Western Region')], default='Central Region', max_length=20)),
                ('county', models.CharField(choices=[('001', 'Mombasa'), ('002', 'Kwale'), ('003', 'Kilifi'), ('004', 'Tana River'), ('005', 'Lamu'), ('006', 'Taita-Taveta'), ('007', 'Garissa'), ('008', 'Wajir'), ('009', 'Mandera'), ('010', 'Marsabit'), ('011', 'Isiolo'), ('012', 'Meru'), ('013', 'Tharaka-Nithi'), ('014', 'Embu'), ('015', 'Kitui'), ('016', 'Machakos'), ('017', 'Makueni'), ('018', 'Nyandarua'), ('019', 'Nyeri'), ('020', 'Kirinyaga'), ('021', "Murang'a"), ('022', 'Kiambu'), ('023', 'Turkana'), ('024', 'West Pokot'), ('025', 'Samburu'), ('026', 'Trans-Nzoia'), ('027', 'Uasin Gishu'), ('028', 'Elgeyo-Marakwet'), ('029', 'Nandi'), ('030', 'Baringo'), ('031', 'Laikipia'), ('032', 'Nakuru'), ('033', 'Narok'), ('034', 'Kajiado'), ('035', 'Kericho'), ('036', 'Bomet'), ('037', 'Kakamega'), ('038', 'Vihiga'), ('039', 'Bungoma'), ('040', 'Busia'), ('041', 'Siaya'), ('042', 'Kisumu'), ('043', 'Homa Bay'), ('044', 'Migori'), ('045', 'Kisii'), ('046', 'Nyamira'), ('047', 'Nairobi')], default='mombasa', max_length=100)),
            ],
        ),
    ]
