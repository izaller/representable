# Generated by Django 2.2.13 on 2020-12-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0064_merge_20201201_1831"),
    ]

    operations = [
        migrations.AddField(
            model_name="drive",
            name="require_user_addresses",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="city",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="state",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="street",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
        migrations.AlterField(
            model_name="address",
            name="zipcode",
            field=models.CharField(blank=True, default="", max_length=12),
        ),
    ]
