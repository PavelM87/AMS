# Generated by Django 3.1.7 on 2021-03-26 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wind', models.CharField(choices=[('0', '0'), ('1-2', '1-2'), ('2-3', '2-3')], default='0', max_length=3, verbose_name='Ветер')),
                ('weather_today', models.CharField(choices=[('sunny', 'солнечно'), ('cloudy', 'облачно'), ('murky', 'пасмурно')], default='солнечно', max_length=6, verbose_name='Погода в день измерений')),
                ('ground', models.CharField(choices=[('podzolic', 'подзолистый'), ('sandy', 'песчаный'), ('clay', 'глинистый'), ('clay_loam', 'суглинок'), ('peat', 'торф'), ('suspension', 'суспесь'), ('on_the_roof', 'установлена на кровле')], default='подзолистый', max_length=11, verbose_name='Грунт')),
                ('temperature', models.CharField(choices=[('0', '0'), ('1-2', '1-2'), ('2-3', '2-3')], default='0', max_length=3, verbose_name='Температура')),
                ('weather_3_days', models.CharField(choices=[('sunny', 'солнечно'), ('cloudy', 'облачно'), ('murky', 'пасмурно')], default='солнечно', max_length=6, verbose_name='Погода в последние 3 дня')),
                ('supply_voltage_COM', models.CharField(choices=[('48', '48'), ('220', '220')], default='48', max_length=3, verbose_name='Питающее напряжение СОМ')),
                ('cable_brand_type', models.CharField(choices=[('vvg', 'ВВГ'), ('pvs', 'ПВС'), ('shvvp', 'ШВВП')], default='ВВГ', max_length=10, verbose_name='Марка кабеля СОМ (тип слева)')),
                ('cable_brand_size', models.CharField(choices=[('2x1.5', '2x1.5'), ('2x2.5', '2x2.5'), ('2x3.5', '2x3.5')], default='2x1.5', max_length=10, verbose_name='Марка кабеля СОМ (сечение справа)')),
                ('cable_lightning_rod', models.CharField(choices=[('metal_strip', 'металлическая полоса'), ('metal_rope', 'металлический трос')], default='металлическая полоса', max_length=20, verbose_name='Молниеприемник – трос молниеприемника')),
                ('ground_loop_bus', models.CharField(choices=[('metal_strip', 'металлическая полоса'), ('metal_rope', 'металлический трос')], default='металлическая полоса', max_length=20, verbose_name='шина (проводник) контура заземления')),
                ('equipment_type', models.CharField(choices=[('panel_antenna', 'панельная антенна'), ('RRL_antenna', 'РРЛ антенна'), ('radio_module', 'радиомодуль')], default='панельная антенна', max_length=20, verbose_name='Тип')),
                ('equipment_height', models.IntegerField(blank=True, null=True)),
                ('equipment_proportions', models.IntegerField(blank=True, null=True)),
                ('equipment_amount', models.IntegerField(blank=True, null=True)),
                ('equipment_manufacturer', models.CharField(blank=True, max_length=50)),
                ('equipment_model', models.CharField(blank=True, max_length=50)),
                ('equipment_note', models.CharField(blank=True, max_length=100)),
                ('ams_schema', models.ImageField(blank=True, upload_to='')),
                ('location_on_map', models.ImageField(blank=True, upload_to='')),
                ('ams', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ams.ams', verbose_name='Объект / наряд')),
                ('equipment_operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ams.operator')),
            ],
        ),
    ]
