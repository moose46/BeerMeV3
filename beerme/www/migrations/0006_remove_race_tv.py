# Generated by Django 4.1.7 on 2023-03-07 13:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0005_race_tv_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="race",
            name="tv",
        ),
    ]
