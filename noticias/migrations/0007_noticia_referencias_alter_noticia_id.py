# Generated by Django 5.0.2 on 2024-05-09 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='referencias',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]