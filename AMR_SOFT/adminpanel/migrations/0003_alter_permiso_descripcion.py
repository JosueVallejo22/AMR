# Generated by Django 5.0.1 on 2024-10-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_alter_permiso_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='descripcion',
            field=models.CharField(max_length=10),
        ),
    ]
