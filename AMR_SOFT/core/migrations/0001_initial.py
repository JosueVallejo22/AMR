# Generated by Django 5.0.1 on 2024-10-24 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=15, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=30)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(max_length=30)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permiso', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.CharField(max_length=10, unique=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(max_length=30, unique=True)),
                ('abreviatura', models.CharField(max_length=5, unique=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
                ('posicion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.posicion')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=50, unique=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCualidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cualidad', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Cualidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cualidad', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(max_length=128)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
                ('tipo_cualidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipocualidad')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('contrasena', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fecha_nac', models.DateField()),
                ('altura', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pierna_habil', models.CharField(max_length=3)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.pais')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.puesto')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jugadores_creados', to='core.usuario')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jugadores_eliminados', to='core.usuario')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jugadores_actualizados', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='RolPermiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateTimeField(auto_now_add=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.estado')),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.permiso')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.rol')),
            ],
            options={
                'unique_together': {('rol', 'permiso')},
            },
        ),
    ]