# Generated by Django 3.2.16 on 2023-03-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='security_question',
            field=models.CharField(default='What is your Society Name?', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='circulars',
            name='filename',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='circulars',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=15),
        ),
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=15),
        ),
        migrations.AlterField(
            model_name='eventphotos',
            name='photopath',
            field=models.FileField(upload_to='eventphoto/'),
        ),
        migrations.AlterField(
            model_name='login',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=15),
        ),
        migrations.AlterField(
            model_name='login',
            name='usertype',
            field=models.CharField(choices=[('security', 'Security'), ('owner', 'Owner'), ('rentee', 'Rentee'), ('admin', 'Admin')], default='Rentee', max_length=15),
        ),
        migrations.AlterField(
            model_name='rentee',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=15),
        ),
        migrations.AlterField(
            model_name='security',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=15),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=15),
        ),
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='Active', max_length=15),
        ),
    ]