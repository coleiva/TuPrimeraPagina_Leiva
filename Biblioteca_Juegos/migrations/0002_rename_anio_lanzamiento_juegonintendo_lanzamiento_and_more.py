# Generated by Django 5.2.3 on 2025-06-14 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca_Juegos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juegonintendo',
            old_name='anio_lanzamiento',
            new_name='lanzamiento',
        ),
        migrations.RenameField(
            model_name='juegopc',
            old_name='anio_lanzamiento',
            new_name='lanzamiento',
        ),
        migrations.RenameField(
            model_name='juegosony',
            old_name='anio_lanzamiento',
            new_name='lanzamiento',
        ),
    ]
