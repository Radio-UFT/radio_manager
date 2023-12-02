# Generated by Django 4.2.7 on 2023-11-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Programa",
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
                ("nome", models.CharField(max_length=100)),
                ("descricao", models.TextField(max_length=500)),
                ("horario", models.TimeField()),
                ("foto", models.ImageField(blank=True, upload_to="programa/fotos")),
            ],
        ),
    ]