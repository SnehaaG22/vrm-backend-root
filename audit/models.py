from django.db import models
from apps.accounts.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
