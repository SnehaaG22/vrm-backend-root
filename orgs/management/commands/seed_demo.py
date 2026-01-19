from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.orgs.models import Org
from apps.accounts.models import User
from apps.vendors.models import Vendor
from apps.templates.models import Template
from apps.assessments.models import Assessment
from apps.evidence.models import Evidence
from apps.remediations.models import Remediation


class Command(BaseCommand):
    help = "Seed demo data for VRM system"

    def handle(self, *args, **options):
        self.stdout.write("Starting demo data seeding...")

        # ---------- ORG ----------
        org, _ = Org.objects.get_or_create(
            name="Demo Org",
            defaults={"domain": "demo.com"}
        )
        self.stdout.write(self.style.SUCCESS("Org created: Demo Org"))

        # ---------- USERS ----------
        users = [
            ("admin", "admin@demo.com", "admin"),
            ("reviewer", "reviewer@demo.com", "reviewer"),
            ("requester", "requester@demo.com", "requester"),
        ]

        for username, email, role in users:
            User.objects.get_or_create(
                username=username,
                defaults={
                    "email": email,
                    "role": role,
                    "org": org,
                    "is_staff": role == "admin",
                    "is_superuser": role == "admin",
                }
            )
            self.stdout.write(self.style.SUCCESS(f"User created: {username} ({role})"))

        # ---------- VENDORS ----------
        vendors = []
        for name in ["AWS", "Stripe"]:
            vendor, _ = Vendor.objects.get_or_create(
                name=name,
                defaults={"org": org}
            )
            vendors.append(vendor)
            self.stdout.write(self.style.SUCCESS(f"Vendor created: {name}"))

        # ---------- TEMPLATE ----------
        template, _ = Template.objects.get_or_create(
            org=org,
            name="Demo Template",
            version=1
        )
        self.stdout.write(self.style.SUCCESS("Template created: Demo Template"))

        # ---------- ASSESSMENTS ----------
        a1, _ = Assessment.objects.get_or_create(
            org=org,
            vendor=vendors[0],
            status="submitted"
        )

        a2, _ = Assessment.objects.get_or_create(
            org=org,
            vendor=vendors[1],
            status="draft"
        )

        self.stdout.write(self.style.SUCCESS("Assessments created"))

        # ---------- EVIDENCE ----------
        evidence_expiry = timezone.now() + timezone.timedelta(days=30)

        Evidence.objects.get_or_create(
            assessment=a1,
            file_name="soc2_report.pdf",
            defaults={
                "expiry_date": evidence_expiry,
            }
        )

        self.stdout.write(self.style.SUCCESS("Evidence created"))

        # ---------- REMEDIATION ----------
        Remediation.objects.get_or_create(
            assessment=a1,
            defaults={
                "status": "open",
            }
        )

        self.stdout.write(self.style.SUCCESS("Remediation created"))

        self.stdout.write(
            self.style.SUCCESS(" Demo data seeding completed successfully!")
        )
