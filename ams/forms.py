from django import forms
from .models import AMS


class AMSModelForm(forms.ModelForm):
    class Meta:
        model = AMS
        fields = '__all__'
