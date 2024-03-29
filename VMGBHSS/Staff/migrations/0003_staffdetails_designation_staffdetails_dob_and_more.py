# Generated by Django 4.2.9 on 2024-02-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0002_staffdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdetails',
            name='designation',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='staffdetails',
            name='dob',
            field=models.CharField(default='NULL', max_length=15),
        ),
        migrations.AddField(
            model_name='staffdetails',
            name='experience',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AddField(
            model_name='staffdetails',
            name='join_data',
            field=models.CharField(default='NULL', max_length=15),
        ),
        migrations.AddField(
            model_name='staffdetails',
            name='qualification',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='staffdetails',
            name='salary',
            field=models.CharField(default='NULL', max_length=10),
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='address',
            field=models.TextField(default='NULL', max_length=15),
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='email',
            field=models.EmailField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='staffdetails',
            name='nationality',
            field=models.CharField(default='NULL', max_length=50),
        ),
    ]
