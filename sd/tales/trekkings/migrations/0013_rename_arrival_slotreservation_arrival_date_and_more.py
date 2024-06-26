# Generated by Django 5.0.3 on 2024-04-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkings', '0012_slotreservation_alter_book_arrival_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slotreservation',
            old_name='arrival',
            new_name='arrival_date',
        ),
        migrations.RenameField(
            model_name='slotreservation',
            old_name='leaving',
            new_name='leaving_date',
        ),
        migrations.AlterField(
            model_name='slotreservation',
            name='number_of_members',
            field=models.CharField(choices=[('2 to 4', '2 to 4'), ('4 to 6', '4 to 6'), ('6 to 10', '6 to 10')], max_length=50),
        ),
    ]
