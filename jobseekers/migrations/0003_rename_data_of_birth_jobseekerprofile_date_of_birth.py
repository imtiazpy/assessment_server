# Generated by Django 4.1.7 on 2023-03-11 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekers', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobseekerprofile',
            old_name='data_of_birth',
            new_name='date_of_birth',
        ),
    ]
