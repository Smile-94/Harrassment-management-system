# Generated by Django 4.1.7 on 2023-04-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]