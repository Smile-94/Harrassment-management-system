# Generated by Django 4.1.7 on 2023-04-03 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('BCSE', 'BCSE'), ('BSCE', 'BSCE'), ('BSME', 'BSME'), ('BSEEE', 'BSEEE'), ('BBA', 'BBA'), ('BSN', 'BSN'), ('BATHM', 'BATHM'), ('BSAg', 'BSAg'), ('BSAg', 'BSAg'), ('BAEcon', 'BAEcon'), ('BA English', 'BA English'), ('MBA', 'MBA'), ('MPH', 'MPH')], max_length=10)),
                ('student_phone', models.CharField(max_length=15)),
                ('national_id', models.CharField(max_length=15)),
                ('father_name', models.CharField(max_length=50)),
                ('father_occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('mother_name', models.CharField(max_length=50)),
                ('mother_occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('gardian_name', models.CharField(blank=True, max_length=50, null=True)),
                ('relation_with', models.CharField(blank=True, max_length=50, null=True)),
                ('gardian_occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('gardian_phone', models.CharField(max_length=15)),
                ('dob', models.DateTimeField()),
                ('photo', models.ImageField(upload_to='medai/student')),
                ('info_of', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]