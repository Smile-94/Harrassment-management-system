# Generated by Django 4.1.7 on 2023-04-13 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_studentinfo_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='dob',
        ),
    ]