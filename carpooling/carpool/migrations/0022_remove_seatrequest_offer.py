# Generated by Django 2.2.1 on 2019-05-25 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0021_auto_20190524_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatrequest',
            name='offer',
        ),
    ]