# Generated by Django 5.0.2 on 2024-02-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reportero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellidos', models.CharField(max_length=80)),
                ('telefono', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
    ]