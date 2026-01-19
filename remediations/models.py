from django.db import models
from apps.assessments.models import Assessment

class Remediation(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
