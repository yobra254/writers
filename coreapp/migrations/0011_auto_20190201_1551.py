# Generated by Django 2.0.10 on 2019-02-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0010_auto_20190201_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='email_address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]