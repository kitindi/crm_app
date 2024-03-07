# Generated by Django 5.0.3 on 2024-03-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Out of delivery", "Out of delivery"),
                            ("Delivered", "Delivered"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=200, null=True)),
                (
                    "product_category",
                    models.CharField(
                        choices=[
                            ("Consumer Electronics", "Consumer Electronics"),
                            ("Home & Garden", "Home & Garden"),
                            ("Men Clothings", "Men Clothings"),
                            ("Accessories", "Accessories"),
                            ("Shoes", "Shoes"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("quantity", models.IntegerField(null=True)),
                (
                    "cost",
                    models.DecimalField(decimal_places=2, max_digits=9, null=True),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=9, null=True),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]