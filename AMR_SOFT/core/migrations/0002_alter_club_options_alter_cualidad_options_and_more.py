# Generated by Django 5.0.1 on 2024-10-24 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'verbose_name_plural': 'Clubes'},
        ),
        migrations.AlterModelOptions(
            name='cualidad',
            options={'verbose_name_plural': 'Cualidades'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='jugador',
            options={'verbose_name_plural': 'Jugadores'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='permiso',
            options={'verbose_name_plural': 'Permisos'},
        ),
        migrations.AlterModelOptions(
            name='posicion',
            options={'verbose_name_plural': 'Posiciones'},
        ),
        migrations.AlterModelOptions(
            name='puesto',
            options={'verbose_name_plural': 'Puestos'},
        ),
        migrations.AlterModelOptions(
            name='rol',
            options={'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='rolpermiso',
            options={'verbose_name_plural': 'roles y permisos'},
        ),
        migrations.AlterModelOptions(
            name='tipocualidad',
            options={'verbose_name_plural': 'Tipo Cualidades'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'Jugadores'},
        ),
    ]