from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser, Team


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'role', 'phone_number', 'comment')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'role', 'phone_number', 'comment')


class UserModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'role', 'phone_number', 'comment', 'is_active')


class TeamsModelForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('member',)