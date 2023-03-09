# Generated by Django 4.1.7 on 2023-03-07 03:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0003_alter_bet_options_alter_race_options_race_tv_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tv",
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
                ("name", models.CharField(default="FOX", max_length=24, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="race",
            name="tv",
            field=models.CharField(default="FOX", max_length=32),
        ),
    ]