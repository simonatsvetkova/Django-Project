# Generated by Django 2.2.1 on 2019-05-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0002_auto_20190521_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='start_location',
            field=models.CharField(choices=[('Bakston', 'Bakston'), ('Banishora', 'Banishora'), ('Beli brezi', 'Beli brezi'), ('Benkovski', 'Benkovski'), ('Borovo', 'Borovo'), ('Botunec', 'Botunec'), ('Boyana', 'Boyana'), ('Chelopechene', 'Chelopechene'), ('Darvenica', 'Darvenica'), ('Dianabad', 'Dianabad'), ('Dragalevci', 'Dragalevci'), ('Druzhba 1', 'Druzhba 1'), ('Druzhba 2', 'Druzhba 2'), ('Fakulteta', 'Fakulteta'), ('Filipovci', 'Filipovci'), ('Geo Milev', 'Geo Milev'), ('Gorna Banya', 'Gorna Banya'), ('Gorublyane', 'Gorublyane'), ('Goce Delchev', 'Goce Delchev'), ('Hadzhi Dimitar', 'Hadzhi Dimitar'), ('Hipodruma', 'Hipodruma'), ('Hladilnika', 'Hladilnika'), ('Hristo Botev', 'Hristo Botev'), ('Iliyanci', 'Iliyanci'), ('Ivan Vazov', 'Ivan Vazov'), ('Izgrev', 'Izgrev'), ('Iztok', 'Iztok'), ('Knyazhevo', 'Knyazhevo'), ('Krasna polyana', 'Krasna polyana'), ('Krasno selo', 'Krasno selo'), ('Kremikovci', 'Kremikovci'), ('Lagera', 'Lagera'), ('Levski', 'Levski'), ('Lozenec', 'Lozenec'), ('Lyulin 1', 'Lyulin 1'), ('Lyulin 2', 'Lyulin 2'), ('Lyulin 3', 'Lyulin 3'), ('Lyulin 4', 'Lyulin 4'), ('Lyulin 5', 'Lyulin 5'), ('Lyulin 6', 'Lyulin 6'), ('Lyulin 7', 'Lyulin 7'), ('Lyulin 8', 'Lyulin 8'), ('Lyulin 9', 'Lyulin 9'), ('Lyulin 10', 'Lyulin 10'), ('Malashevci', 'Malashevci'), ('Malinova Dolina', 'Malinova Dolina'), ('Manastirski livadi', 'Manastirski livadi'), ('Mladost 1', 'Mladost 1'), ('Mladost 2', 'Mladost 2'), ('Mladost 3', 'Mladost 3'), ('Mladost 4', 'Mladost 4'), ('Moderno predgradie', 'Moderno predgradie'), ('Motopista', 'Motopista'), ('Musagenica', 'Musagenica'), ('Nadezhda', 'Nadezhda'), ('Nadezhda 3', 'Nadezhda 3'), ('Nadezhda 6', 'Nadezhda 6'), ('Obelya', 'Obelya'), ('Obelya 2', 'Obelya 2'), ('Ovcha kupel', 'Ovcha kupel'), ('Ovcha kupel 2', 'Ovcha kupel 2'), ('Pavlovo', 'Pavlovo'), ('Poduyane', 'Poduyane'), ('Poligona', 'Poligona'), ('Reduta', 'Reduta'), ('Republika', 'Republika'), ('Seslavci', 'Seslavci'), ('Simeonovo', 'Simeonovo'), ('Slatina', 'Slatina'), ('Stefan Karadzha', 'Stefan Karadzha'), ('Strelbishte', 'Strelbishte'), ('Studentski grad', 'Studentski grad'), ('Suhata reka', 'Suhata reka'), ('Suhodol', 'Suhodol'), ('Sveta Troica', 'Sveta Troica'), ('Trebich', 'Trebich'), ('Vrazhdebna', 'Vrazhdebna'), ('Yavorov', 'Yavorov'), ('Zaharna Fabrika', 'Zaharna Fabrika'), ('Zapaden park', 'Zapaden park'), ('Zona B-5', 'Zona B-5'), ('Zona B-18', 'Zona B-18'), ('Zona B-19', 'Zona B-19')], default='choose start location', max_length=50),
        ),
    ]