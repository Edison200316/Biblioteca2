# Generated by Django 5.1.4 on 2024-12-16 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('codigof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_libros.libro')),
                ('cedulaf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_libros.usuario')),
            ],
        ),
    ]