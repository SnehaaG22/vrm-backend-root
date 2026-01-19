#VRM/TPRM Backend – Django + DRF + PostgreSQL

Overview:
This repository provides the backend foundation for a Vendor Risk Management (VRM) / Third-Party Risk Management (TPRM) system built with Django, Django REST Framework, and PostgreSQL.
It supports multi-tenant organizations, RBAC permissions, audit logging, and comes with a demo data seeding command for easy setup.

Features:

Multi-tenant support (org_id scoped models).

Role-based access control (Admin, Reviewer, Requester, Vendor).

Audit logging for critical write actions.

Models for:
accounts: Users, roles, permissions

orgs: Tenants

vendors + vendor users

templates + sections + questions + template versions

assessments + responses

evidence with expiry dates

reviews, findings, remediations

renewals
audit_logs

Demo data seeding (manage.py seed_demo)

Docker Compose setup (Postgres + Redis + optional pgAdmin)

Swagger/OpenAPI docs via drf-spectacular

Quick Setup

1) Docker Setup:
   
docker compose up -d

Services: postgres, redis, optional pgadmin

3) Django Setup:
   
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

5) Seed Demo Data:
   
   python manage.py seed_demo

This will create:

1 organization (Demo Org)

3 users: admin, reviewer, requester

2 vendors + vendor users

1 template + 2 sections + sample questions

2 assessments in different statuses

1 remediation example + evidence expiry

4) Run Development Server:
   
   python manage.py runserver
