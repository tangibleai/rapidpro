# Generated by Django 2.2.4 on 2019-10-23 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("airtime", "0013_recipient_to_urn")]

    operations = [
        migrations.AlterField(
            model_name="airtimetransfer",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="airtime_transfers", to="contacts.Contact"
            ),
        )
    ]