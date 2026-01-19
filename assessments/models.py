from django.db import models
from apps.orgs.models import Org
from apps.vendors.models import Vendor

class Assessment(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="draft")

class Response(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer = models.TextField()
