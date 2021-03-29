import django_filters
from django_filters import CharFilter, BooleanFilter

from .models import Order


class OrderAddressFilter(django_filters.FilterSet):
    address = CharFilter(lookup_expr='icontains')
    in_work = BooleanFilter(field_name='team', lookup_expr='isnull',exclude=True)

    class Meta:
        model = Order
        fields = ['country', 'region', 'city', 'team']
