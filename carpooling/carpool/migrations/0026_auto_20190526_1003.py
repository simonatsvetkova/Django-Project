# Generated by Django 2.2.1 on 2019-05-26 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0025_auto_20190525_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatrequest',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='seatrequest',
            name='passenger',
        ),
    ]
