# Generated by Django 5.0.2 on 2024-04-18 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_reportero_acta_nacimineto_reportero_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportero',
            old_name='acta_nacimineto',
            new_name='acta_nacimiento',
        ),
    ]
