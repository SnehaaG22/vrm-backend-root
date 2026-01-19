# apps/templates/models.py
from django.db import models
from apps.orgs.models import Org

class Template(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    version = models.PositiveIntegerField(default=1)  # <-- add this field

    def __str__(self):
        return f"{self.name} v{self.version}"
