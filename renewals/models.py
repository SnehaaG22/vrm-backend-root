from django.db import models
from apps.vendors.models import Vendor

class Renewal(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    renewal_date = models.DateField()
