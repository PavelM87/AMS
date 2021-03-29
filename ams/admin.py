from django.contrib import admin
from .models import (
    AMS, Operator, Country, Region, City, AMSType
)


admin.site.register(AMS)
admin.site.register(Operator)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(AMSType)
