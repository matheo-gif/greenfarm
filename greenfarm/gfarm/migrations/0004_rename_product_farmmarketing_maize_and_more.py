# Generated by Django 4.2.5 on 2023-09-26 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gfarm', '0003_rename_second_name_farmers_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmmarketing',
            old_name='product',
            new_name='Maize',
        ),
        migrations.RenameField(
            model_name='farmmarketing',
            old_name='marketing_end_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='farmmarketing',
            old_name='marketing_method',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='farmmarketing',
            name='marketing_conversions',
        ),
        migrations.RemoveField(
            model_name='farmmarketing',
            name='marketing_reach',
        ),
        migrations.RemoveField(
            model_name='farmmarketing',
            name='marketing_start_date',
        ),
        migrations.RemoveField(
            model_name='farmproduct',
            name='name',
        ),
        migrations.AddField(
            model_name='farmproduct',
            name='Maize_Variety',
            field=models.CharField(choices=[('01', 'H614'), ('02', 'H512'), ('03', 'H513'), ('04', 'DH02'), ('05', 'DH03'), ('06', 'DH04'), ('07', 'H624'), ('08', 'H621'), ('10', 'H617'), ('11', 'H614'), ('12', 'H615'), ('13', 'H621'), ('14', 'H614'), ('15', 'H515'), ('16', 'H513'), ('17', 'PHB 3253'), ('18', 'PHB 30M35')], default='H614', max_length=100),
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('Central', 'Central Region'), ('Coast', 'Coast Region'), ('Eastern', 'Eastern Region'), ('Nairobi', 'Nairobi Region'), ('North Eastern', 'North Eastern Region'), ('Nyanza', 'Nyanza Region'), ('Rift Valley', 'Rift Valley Region'), ('Western', 'Western Region')], default='Central Region', max_length=20)),
                ('county', models.CharField(choices=[('001', 'Mombasa'), ('002', 'Kwale'), ('003', 'Kilifi'), ('004', 'Tana River'), ('005', 'Lamu'), ('006', 'Taita-Taveta'), ('007', 'Garissa'), ('008', 'Wajir'), ('009', 'Mandera'), ('010', 'Marsabit'), ('011', 'Isiolo'), ('012', 'Meru'), ('013', 'Tharaka-Nithi'), ('014', 'Embu'), ('015', 'Kitui'), ('016', 'Machakos'), ('017', 'Makueni'), ('018', 'Nyandarua'), ('019', 'Nyeri'), ('020', 'Kirinyaga'), ('021', "Murang'a"), ('022', 'Kiambu'), ('023', 'Turkana'), ('024', 'West Pokot'), ('025', 'Samburu'), ('026', 'Trans-Nzoia'), ('027', 'Uasin Gishu'), ('028', 'Elgeyo-Marakwet'), ('029', 'Nandi'), ('030', 'Baringo'), ('031', 'Laikipia'), ('032', 'Nakuru'), ('033', 'Narok'), ('034', 'Kajiado'), ('035', 'Kericho'), ('036', 'Bomet'), ('037', 'Kakamega'), ('038', 'Vihiga'), ('039', 'Bungoma'), ('040', 'Busia'), ('041', 'Siaya'), ('042', 'Kisumu'), ('043', 'Homa Bay'), ('044', 'Migori'), ('045', 'Kisii'), ('046', 'Nyamira'), ('047', 'Nairobi')], default='mombasa', max_length=100)),
                ('Maize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gfarm.farmproduct')),
            ],
        ),
    ]