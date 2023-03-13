# Generated by Django 4.1.7 on 2023-03-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0011_weeklybets_result"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="driver_id",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="www.driver"
            ),
        ),
        migrations.AddField(
            model_name="result",
            name="finished",
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterUniqueTogether(
            name="result",
            unique_together={("race_id", "driver_id", "finished")},
        ),
    ]
