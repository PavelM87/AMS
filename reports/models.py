from django.db import models
from datetime import date
from ams.models import AMS, Operator
from users.models import Team


class Report(models.Model):
    ams = models.ForeignKey(AMS, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Объект / наряд')
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    wind = models.CharField(choices=(
            ('0', '0'),
            ('1-2', '1-2'),
            ('2-3', '2-3')
        ), max_length=3, default='0', verbose_name='Ветер')
    weather_today = models.CharField(choices=(
            ('sunny', 'солнечно'),
            ('cloudy', 'облачно'),
            ('murky', 'пасмурно')
        ), max_length=6, default='солнечно', verbose_name='Погода в день измерений')
    ground = models.CharField(choices=(
            ('podzolic', 'подзолистый'),
            ('sandy', 'песчаный'),
            ('clay', 'глинистый'),
            ('clay_loam', 'суглинок'),
            ('peat', 'торф'),
            ('suspension', 'суспесь'),
            ('on_the_roof', 'установлена на кровле')
        ), max_length=11, default='подзолистый', verbose_name='Грунт')
    temperature = models.CharField(choices=(
            ('0', '0'),
            ('1-2', '1-2'),
            ('2-3', '2-3')
        ), max_length=3, default='0', verbose_name='Температура')
    weather_3_days = models.CharField(choices=(
            ('sunny', 'солнечно'),
            ('cloudy', 'облачно'),
            ('murky', 'пасмурно')
        ), max_length=6, default='солнечно', verbose_name='Погода в последние 3 дня')
    supply_voltage_COM = models.CharField(choices=(
            ('48', '48'),
            ('220', '220'),
        ), max_length=3, default='48', verbose_name='Питающее напряжение СОМ')
    cable_brand_type = models.CharField(choices=(
            ('vvg', 'ВВГ'),
            ('pvs', 'ПВС'),
            ('shvvp', 'ШВВП')
        ), max_length=10, default='ВВГ', verbose_name='Марка кабеля СОМ (тип слева)')
    cable_brand_size = models.CharField(choices=(
            ('2x1.5', '2x1.5'),
            ('2x2.5', '2x2.5'),
            ('2x3.5', '2x3.5')
        ), max_length=10, default='2x1.5', verbose_name='Марка кабеля СОМ (сечение справа)')
    cable_lightning_rod = models.CharField(choices=(
            ('metal_strip', 'металлическая полоса'),
            ('metal_rope', 'металлический трос'),
        ), max_length=20, default='металлическая полоса', verbose_name='Молниеприемник – трос молниеприемника')
    ground_loop_bus = models.CharField(choices=(
            ('metal_strip', 'металлическая полоса'),
            ('metal_rope', 'металлический трос'),
        ), max_length=20, default='металлическая полоса', verbose_name='шина (проводник) контура заземления')
    # Оборудование на АМС / Проактуализируйте
    equipment_type = models.CharField(choices=(
            ('panel_antenna', 'панельная антенна'),
            ('RRL_antenna', 'РРЛ антенна'),
            ('radio_module', 'радиомодуль'),
        ), max_length=20, default='панельная антенна', verbose_name='Тип')
    equipment_height = models.IntegerField(null=True, blank=True)
    equipment_proportions = models.IntegerField(null=True, blank=True)
    equipment_amount = models.IntegerField(null=True, blank=True)
    equipment_manufacturer = models.CharField(max_length=50, blank=True)
    equipment_model = models.CharField(max_length=50, blank=True)
    equipment_operator = models.ForeignKey(Operator, null=True, blank=True, on_delete=models.SET_NULL)
    equipment_note = models.CharField(max_length=100, blank=True)
    ams_schema = models.ImageField(blank=True)
    location_on_map = models.ImageField(blank=True)

    def __str__(self):
        return f"Отчет № {self.id}"

