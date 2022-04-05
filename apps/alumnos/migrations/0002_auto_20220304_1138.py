# Generated by Django 2.1 on 2022-03-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='cedula',
            field=models.CharField(max_length=10, verbose_name='Cedula'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Foto'),
        ),
    ]