# Generated by Django 3.2.23 on 2023-11-27 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='adress',
            new_name='phone',
        ),
    ]
