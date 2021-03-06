# Generated by Django 2.2.10 on 2020-09-29 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0141_help_text_cleanup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="msg",
            name="topup",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="msgs",
                to="orgs.TopUp",
            ),
        ),
    ]
