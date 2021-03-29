from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        MODERATOR = 'MOD', _('Moderator')
        SPECIALIST = 'SPC', _('Specialist')
        SUPERUSER = 'SUP', _('Superuser')

    username = models.CharField(_('username'), max_length=60)
    role = models.CharField(_('user rights'), max_length=3, choices=Role.choices, default=Role.SPECIALIST)
    phone_number = models.CharField(_('phone number'), max_length=30, blank=True)
    comment = models.TextField(_('comment'), blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Team(models.Model):
    member = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f"{self.member.all()[0].username}, {self.member.all()[1].username}"

    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"
