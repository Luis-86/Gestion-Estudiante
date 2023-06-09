# Generated by Django 4.1.7 on 2023-03-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_carrera', models.CharField(choices=[('001', 'DESARROLLO DE SOFTWARE'), ('002', 'CONTABILIDAD Y AUDITORIA')], max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_matricula', models.IntegerField()),
                ('genero', models.CharField(max_length=10)),
                ('ciclo', models.IntegerField()),
                ('periodo_academico', models.CharField(max_length=50)),
                ('fecha_matricula', models.DateField()),
                ('fk_Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_istam.carrera')),
                ('fk_Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_istam.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_istam.docente')),
            ],
        ),
    ]
