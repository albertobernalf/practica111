# Generated by Django 2.1.15 on 2022-09-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0004_auto_20220901_1126'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dependencias',
            unique_together={('sedesClinica', 'serviciosSedes', 'servicios', 'subServicios', 'numero', 'dependenciasTipo')},
        ),
    ]