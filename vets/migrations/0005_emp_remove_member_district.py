# Generated by Django 4.0.3 on 2023-01-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vets', '0004_alter_member_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.TextField()),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_mobile', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='District',
        ),
    ]
