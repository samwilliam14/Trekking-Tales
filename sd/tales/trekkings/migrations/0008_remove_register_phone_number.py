# Generated by Django 5.0.3 on 2024-03-28 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trekkings', '0007_rename_password1_register_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='phone_number',
        ),
    ]
