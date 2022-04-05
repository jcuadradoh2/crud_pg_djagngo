# Generated by Django 2.1 on 2022-03-04 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cedula')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('X', 'GLBTI+')], default='M', max_length=1, verbose_name='Genero')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
    ]
