# Generated by Django 2.1.15 on 2022-09-01 21:17

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0007_auto_20220901_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencias',
            name='subServicios',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='serviciosSedes', chained_model_field='serviciosSedes', on_delete=django.db.models.deletion.CASCADE, to='sitios.SubServiciosSedes'),
        ),
    ]
