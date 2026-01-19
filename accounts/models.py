from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.orgs.models import Org

class User(AbstractUser):
    org = models.ForeignKey(Org, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ("admin", "Admin"),
            ("reviewer", "Reviewer"),
            ("requester", "Requester"),
            ("vendor", "Vendor"),
        ],
    )
