# Generated by Django 5.0.4 on 2024-06-12 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eventos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="evento",
            old_name="descricap",
            new_name="descricao",
        ),
    ]
