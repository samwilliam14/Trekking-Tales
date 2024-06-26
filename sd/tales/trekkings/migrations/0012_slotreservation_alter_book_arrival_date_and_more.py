# Generated by Django 5.0.3 on 2024-04-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkings', '0011_alter_book_arrival_date_alter_book_leaving_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('number_of_members', models.CharField(max_length=50)),
                ('arrival', models.DateField()),
                ('leaving', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='arrival_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='leaving_date',
            field=models.DateField(),
        ),
    ]
