# Generated by Django 4.2.3 on 2023-09-14 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_alter_bookinstance_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("m", "Maintenance"),
                    ("o", "On loan"),
                    ("a", "Available"),
                    ("r", "Reserved"),
                ],
                default="m",
                help_text="Book availability",
                max_length=1,
            ),
        ),
    ]