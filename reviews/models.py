from django.db import models
from apps.assessments.models import Assessment

class Review(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    decision = models.CharField(max_length=50)
