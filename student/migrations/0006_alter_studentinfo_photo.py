# Generated by Django 4.1.7 on 2023-04-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_studentinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='photo',
            field=models.ImageField(upload_to='media/student'),
        ),
    ]
