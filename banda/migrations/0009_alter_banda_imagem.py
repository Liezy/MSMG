# Generated by Django 5.0.4 on 2024-06-23 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banda", "0008_banda_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banda",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="banda/imagens/"),
        ),
    ]