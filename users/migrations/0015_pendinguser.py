# Generated by Django 4.2.17 on 2024-12-27 12:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0014_user_is_email_verified"),
    ]

    operations = [
        migrations.CreateModel(
            name="PendingUser",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("username", models.EmailField(max_length=250, unique=True)),
                ("email", models.EmailField(max_length=250, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]