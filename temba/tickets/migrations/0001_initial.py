# Generated by Django 2.2.4 on 2020-04-23 14:38

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import temba.utils.uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contacts", "0108_remove_contact_is_paused"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orgs", "0058_auto_20190723_2129"),
    ]

    operations = [
        migrations.CreateModel(
            name="TicketingService",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Whether this item is active, use this instead of deleting"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was originally created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        editable=False,
                        help_text="When this item was last modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=temba.utils.uuid.uuid4)),
                ("service_type", models.CharField(max_length=16)),
                ("name", models.CharField(max_length=64)),
                ("config", django.contrib.postgres.fields.jsonb.JSONField()),
                (
                    "created_by",
                    models.ForeignKey(
                        help_text="The user which originally created this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tickets_ticketingservice_creations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        help_text="The user which last modified this item",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tickets_ticketingservice_modifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="ticketing_services", to="orgs.Org"
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=temba.utils.uuid.uuid4, unique=True)),
                ("subject", models.TextField()),
                ("body", models.TextField()),
                ("external_id", models.CharField(max_length=255, null=True)),
                ("config", django.contrib.postgres.fields.jsonb.JSONField()),
                ("status", models.CharField(choices=[("O", "Open"), ("C", "Closed")], max_length=1)),
                ("opened_on", models.DateTimeField(default=django.utils.timezone.now)),
                ("modified_on", models.DateTimeField(default=django.utils.timezone.now)),
                ("closed_on", models.DateTimeField(null=True)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="tickets", to="contacts.Contact"
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="tickets", to="orgs.Org"
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tickets",
                        to="tickets.TicketingService",
                    ),
                ),
            ],
        ),
    ]
