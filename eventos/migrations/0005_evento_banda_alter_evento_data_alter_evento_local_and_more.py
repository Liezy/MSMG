# Generated by Django 5.0.4 on 2024-06-15 23:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banda", "0002_evento"),
        ("eventos", "0004_delete_participante"),
    ]

    operations = [
        migrations.AddField(
            model_name="evento",
            name="banda",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventos",
                to="banda.banda",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="evento",
            name="data",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="evento",
            name="local",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="evento",
            name="titulo",
            field=models.CharField(max_length=100),
        ),
    ]
