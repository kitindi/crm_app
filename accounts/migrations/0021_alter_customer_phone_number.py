# Generated by Django 5.0.3 on 2024-03-21 05:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0020_alter_customer_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]