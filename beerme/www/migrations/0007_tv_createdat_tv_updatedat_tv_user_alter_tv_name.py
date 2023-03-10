# Generated by Django 4.1.7 on 2023-03-08 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("www", "0006_remove_race_tv"),
    ]

    operations = [
        migrations.AddField(
            model_name="tv",
            name="createdAt",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="date created"
            ),
        ),
        migrations.AddField(
            model_name="tv",
            name="updatedAt",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="date last updated"
            ),
        ),
        migrations.AddField(
            model_name="tv",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="tv",
            name="name",
            field=models.CharField(
                default="FOX", max_length=24, null=True, unique=True
            ),
        ),
    ]
