from django import forms
from .models import Report, AMSEquipment


class ReportModelForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'ams',
            'team',
            'wind',
            'weather_today',
            'ground',
            'temperature',
            'weather_3_days',
            'equipment_type',
            'equipment_height',
            'equipment_proportions',
            'equipment_amount',
            'equipment_manufacturer',
            'equipment_model',
            'equipment_operator',
            'equipment_note',
            'ams_schema',
            'location_on_map',
        ]

        labels = {
            'ams': 'объект',
            'team': 'Бригада специалистов',
            'wind': 'Ветер',
            'weather_today': 'Погода в день измерений',
            'ground': 'Грунт',
            'temperature': 'Температура',
            'weather_3_days': 'Погода в последние 3 дня',
            'equipment_type': 'Тип',
            'equipment_height': 'Высота',
            'equipment_proportions': 'Размеры',
            'equipment_amount': 'Количество',
            'equipment_manufacturer': 'Производитель',
            'equipment_model': 'Модель',
            'equipment_operator': 'Оператор',
            'equipment_note': 'Примечание',
            'ams_schema': 'Схема объекта',
            'location_on_map': 'Расположение на карте'
        }

        widgets = {
            'equipment_type': forms.Select(attrs={'class': 'formset-field'}),
            'equipment_height': forms.TextInput(attrs={'class': 'formset-field'}),
            'equipment_proportions': forms.TextInput(attrs={'class': 'formset-field'}),
            'equipment_amount': forms.TextInput(attrs={'class': 'formset-field'}),
            'equipment_manufacturer': forms.TextInput(attrs={'class': 'formset-field'}),
            'equipment_model': forms.TextInput(attrs={'class': 'formset-field'}),
            'equipment_operator': forms.Select(attrs={'class': 'formset-field'}),
            'equipment_note': forms.TextInput(attrs={'class': 'formset-field'}),
            'ams_schema': forms.FileInput(attrs={'class': 'formset-field'}),
            'location_on_map': forms.FileInput(attrs={'class': 'formset-field'})
        }


class AMSEquipmentForm(forms.ModelForm):
    class Meta:
        model = AMSEquipment
        fields = [
            'type',
            'height',
            'proportions',
            'amount',
            'manufacturer',
            'model',
            'operator',
            'note',
        ]

        label = {
            'type': 'Тип',
            'height': 'Высота',
            'proportions': 'Размеры',
            'amount': 'Количество',
            'manufacturer': 'Производитель',
            'model': 'Модель',
            'operator': 'Оператор',
            'note': 'Примечание',
        }

        widgets = {
            'type': forms.Select(attrs={'class': 'formset-field'}),
            'height': forms.TextInput(attrs={'class': 'formset-field'}),
            'proportions': forms.TextInput(attrs={'class': 'formset-field'}),
            'amount': forms.TextInput(attrs={'class': 'formset-field'}),
            'manufacturer': forms.TextInput(attrs={'class': 'formset-field'}),
            'model': forms.TextInput(attrs={'class': 'formset-field'}),
            'operator': forms.Select(attrs={'class': 'formset-field'}),
            'note': forms.TextInput(attrs={'class': 'formset-field'}),
        }