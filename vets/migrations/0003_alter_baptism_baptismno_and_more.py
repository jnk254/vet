# Generated by Django 4.0.3 on 2023-01-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vets', '0002_rename_districttype_member_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baptism',
            name='BaptismNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='communicant',
            name='CommunicantNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='Contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='NextofkinContact',
            field=models.IntegerField(),
        ),
    ]