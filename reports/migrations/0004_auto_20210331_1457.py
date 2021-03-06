# Generated by Django 3.1.7 on 2021-03-31 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_amsequipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='equipment_amount',
        ),
        migrations.RemoveField(
            model_name='report',
            name='equipment_height',
        ),
        migrations.RemoveField(
            model_name='report',
            name='equipment_manufacturer',
        ),
        migrations.RemoveField(
            model_name='report',
            name='equipment_model',
        ),
        migrations.RemoveField(
            model_name='report',
            name='equipment_note',
        ),
        migrations.RemoveField(
            model_name='report',
            name='equipment_operator',
        ),
        migrations.RemoveField(
            model_name='report',
            name='equipment_proportions',
        ),
        migrations.RemoveField(
            model_name='report',
            name='equipment_type',
        ),
        migrations.AlterModelTable(
            name='amsequipment',
            table='reports_amsequipment',
        ),
    ]
