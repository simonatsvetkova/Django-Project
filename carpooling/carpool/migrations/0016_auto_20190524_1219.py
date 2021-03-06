# Generated by Django 2.2.1 on 2019-05-24 09:19

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0015_auto_20190524_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='regularity',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('*', 'All'), ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday')], default='*', max_length=21),
        ),
    ]
