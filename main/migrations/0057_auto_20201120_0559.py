# Generated by Django 2.2.13 on 2020-11-20 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0056_auto_20200908_1604"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communityentry",
            name="drive",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="submissions",
                to="main.Drive",
            ),
        ),
        migrations.AlterField(
            model_name="communityentry",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="submissions",
                to="main.Organization",
            ),
        ),
    ]
