from datetime import date
from django.db import models

from ams.models import AMS, Country, City, Region
from users.models import Team


class Order(models.Model):
    date = models.DateField(default=date.today)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=100)
    ams = models.ForeignKey(AMS, null=True, blank=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    planned_works = models.TextField(blank=True)
    contacts = models.TextField(blank=True)
    work_codes = models.TextField(blank=True)

    def __str__(self):
        return f"Наряд № {self.id}"

