from django.db import models
from apps.assessments.models import Assessment

class Evidence(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    expiry_date = models.DateField(null=True, blank=True)
