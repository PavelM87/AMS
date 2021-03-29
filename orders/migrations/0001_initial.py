# Generated by Django 3.1.7 on 2021-03-26 15:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('address', models.CharField(max_length=100)),
                ('planned_works', models.TextField(blank=True)),
                ('contacts', models.TextField(blank=True)),
                ('work_codes', models.TextField(blank=True)),
                ('ams', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ams.ams')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ams.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ams.country')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ams.region')),
            ],
        ),
    ]
