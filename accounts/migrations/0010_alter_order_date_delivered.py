# Generated by Django 5.0.3 on 2024-03-07 07:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0009_order_date_delivered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_delivered",
            field=models.DateField(blank=True, null=True),
        ),
    ]
