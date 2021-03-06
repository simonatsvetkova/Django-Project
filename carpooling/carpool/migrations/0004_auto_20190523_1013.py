# Generated by Django 2.2.1 on 2019-05-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0003_auto_20190523_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='number_of_seats',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6)], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='offer',
            name='regularity',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=15),
        ),
    ]
