from django.db import models


class AMS(models.Model):

    code = models.CharField(max_length=50)
    code_alternative = models.CharField(max_length=50)
    operator = models.ForeignKey("Operator", null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey("Country", null=True, blank=True, on_delete=models.SET_NULL)
    region = models.ForeignKey("Region", null=True, blank=True, on_delete=models.SET_NULL)
    region_code = models.CharField(max_length=50, blank=True)
    city = models.ForeignKey("City", null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=50, blank=True)
    latitude = models.CharField(max_length=50, blank=True)
    longitude = models.CharField(max_length=50, blank=True)
    ams_type = models.ForeignKey("AMSType", null=True, blank=True, on_delete=models.SET_NULL)
    section_type = models.CharField(
        choices=(
            ('square', 'Квадрат'),
            ('triangle', 'Треугольник'),
            ('circle', 'Круг')
        ), max_length=8, default='Квадрат'
    )
    section_length = models.CharField(max_length=50, blank=True)
    ferm_type = models.CharField(
        choices=(
            ('sq_ferm', 'ферма квадратная'),
            ('tr_ferm', 'ферма треугольная'),
            ('pipe', 'труба'),
            ('pillar', 'столб')
        ), max_length=7, default='ферма квадратная'
    )
    ams_height = models.CharField(max_length=50, blank=True)
    signal_lights = models.BooleanField(default=True)
    deviation = models.CharField(max_length=50, blank=True)
    mounting_height = models.CharField(max_length=50, blank=True)
    rope_diameter = models.CharField(max_length=50, blank=True)
    ropes_amount = models.CharField(max_length=50, blank=True)
    pulling = models.CharField(max_length=50, blank=True)
    waterproofing = models.CharField(max_length=50, blank=True)
    ams_manufacturer = models.CharField(max_length=50, blank=True)
    ams_availability_operators = models.CharField(max_length=50, blank=True)
    developer_project_documentation = models.CharField(max_length=50, blank=True)
    ams_schema = models.ImageField( blank=True)
    ams_layout_equipment_schema = models.ImageField(blank=True)
    ams_photos = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.code} {self.code_alternative}"


class Operator(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AMSType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





