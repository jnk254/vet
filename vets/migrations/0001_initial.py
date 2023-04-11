# Generated by Django 4.0.3 on 2023-01-10 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baptism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BaptismNo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Communicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CommunicantNo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DistrictName', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('SecondName', models.CharField(max_length=200)),
                ('Surname', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=10)),
                ('Gender', models.CharField(max_length=10)),
                ('NextofkinName', models.CharField(max_length=200)),
                ('NextofkinContact', models.CharField(max_length=10)),
                ('Age', models.CharField(max_length=5)),
                ('Address', models.CharField(max_length=100)),
                ('DistrictType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vets.district')),
            ],
        ),
    ]