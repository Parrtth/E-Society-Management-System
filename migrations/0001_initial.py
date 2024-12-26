# Generated by Django 3.2.16 on 2023-02-15 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockname', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'tblblock',
            },
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=250)),
                ('complaindate', models.DateField(max_length=15)),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'tblcomplain',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventdate', models.DateField(max_length=12)),
                ('eventtitle', models.CharField(max_length=20)),
                ('fromdate', models.DateField(max_length=15)),
                ('todate', models.DateField(max_length=15)),
            ],
            options={
                'db_table': 'tblevent',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('registerdate', models.DateField(max_length=15)),
            ],
            options={
                'db_table': 'tbllogin',
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencyname', models.CharField(max_length=12)),
                ('personname', models.CharField(max_length=20)),
                ('fromdate', models.DateField(max_length=15)),
                ('todate', models.DateField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login')),
            ],
            options={
                'db_table': 'tblsecurity',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicename', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tblservice',
            },
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceproname', models.CharField(max_length=12)),
                ('servicedetails', models.CharField(max_length=200)),
                ('contactno', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'tblserviceprovider',
            },
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('societyname', models.CharField(max_length=15)),
                ('logo', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'tblsociety',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitno', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('floorno', models.CharField(max_length=15)),
                ('parkingno', models.CharField(max_length=15)),
                ('blockid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.block')),
            ],
            options={
                'db_table': 'tblunit',
            },
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unittype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'tblunittype',
            },
        ),
        migrations.CreateModel(
            name='Visitorentry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitorname', models.CharField(max_length=20)),
                ('mobileno', models.CharField(max_length=12)),
                ('date', models.DateField(max_length=15)),
                ('reason', models.CharField(max_length=60)),
                ('securityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.security')),
                ('unitid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.unit')),
            ],
            options={
                'db_table': 'tblvisitorentry',
            },
        ),
        migrations.CreateModel(
            name='VehicleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleno', models.CharField(max_length=12)),
                ('vehicletype', models.CharField(max_length=15)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login')),
                ('unitid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.unit')),
            ],
            options={
                'db_table': 'tblvehicledetails',
            },
        ),
        migrations.AddField(
            model_name='unit',
            name='unittypeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.unittype'),
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solutiondetails', models.CharField(max_length=300)),
                ('date', models.DateField(max_length=10)),
                ('complainid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.complain')),
            ],
            options={
                'db_table': 'tblsolution',
            },
        ),
        migrations.CreateModel(
            name='Rentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rentagreementdt', models.DateField(max_length=15)),
                ('permanentaddress', models.CharField(max_length=300)),
                ('fromdate', models.DateField(max_length=15)),
                ('todate', models.DateField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login')),
                ('unitid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.unit')),
            ],
            options={
                'db_table': 'tblrentee',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=300)),
                ('shareno', models.CharField(max_length=15)),
                ('registerdate', models.DateField(max_length=15)),
                ('fromdate', models.DateField(max_length=15)),
                ('todate', models.DateField(max_length=15)),
                ('totalfamilymembers', models.CharField(max_length=10)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login')),
                ('unitid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.unit')),
            ],
            options={
                'db_table': 'tblowner',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incometitle', models.CharField(max_length=25)),
                ('incomedetails', models.CharField(max_length=200)),
                ('amount', models.FloatField(max_length=25)),
                ('incomedate', models.DateField(max_length=15)),
                ('Loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login')),
            ],
            options={
                'db_table': 'tblincome',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=100)),
                ('amount', models.FloatField(max_length=25)),
                ('expencedate', models.DateField(max_length=15)),
                ('expencetitle', models.CharField(max_length=15)),
                ('Loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login')),
            ],
            options={
                'db_table': 'tblexpense',
            },
        ),
        migrations.CreateModel(
            name='EventPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photopath', models.CharField(max_length=25)),
                ('eventid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.event')),
            ],
            options={
                'db_table': 'tbleventphotos',
            },
        ),
        migrations.AddField(
            model_name='complain',
            name='Loginid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login'),
        ),
        migrations.AddField(
            model_name='complain',
            name='serviceid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.service'),
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membersname', models.CharField(max_length=12)),
                ('foryear', models.DateField(max_length=15)),
                ('fromdate', models.DateField(max_length=15)),
                ('todate', models.DateField(max_length=15)),
                ('unitid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.unit')),
            ],
            options={
                'db_table': 'tblcommittee',
            },
        ),
        migrations.CreateModel(
            name='circulars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('filename', models.CharField(max_length=25)),
                ('date', models.DateField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('Loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socadmin.login')),
            ],
            options={
                'db_table': 'tblcirculars',
            },
        ),
    ]