# Generated by Django 3.2 on 2022-08-01 13:40

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sitios', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('planta', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialdependencias',
            name='documento',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentohistorialDep', to='usuarios.usuarios'),
        ),
        migrations.AddField(
            model_name='historialdependencias',
            name='tipoDoc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.tiposdocumento'),
        ),
        migrations.AddField(
            model_name='historialdependencias',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.planta'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='dependencias',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.dependencias'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='documento',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='DocumentoDepAct', to='usuarios.usuarios'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='tipoDoc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuarios.tiposdocumento'),
        ),
        migrations.AddField(
            model_name='dependenciasactual',
            name='usuarioRegistro',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='planta.planta'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='dependenciasTipo',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.dependenciastipo'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='sedesClinica',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.sedesclinica'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='servicios',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='sedesClinica', chained_model_field='sedesClinica', on_delete=django.db.models.deletion.CASCADE, to='sitios.serviciossedes'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='serviciosSedes',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='serviciosSedes1', to='sitios.serviciossedes'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='subServicios',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='servicios', chained_model_field='servicios', on_delete=django.db.models.deletion.CASCADE, to='sitios.subserviciossedes'),
        ),
        migrations.AddField(
            model_name='ciudades',
            name='departamentos',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ciudades', to='sitios.departamentos'),
        ),
        migrations.AddField(
            model_name='centros',
            name='ciudades',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='departamentos', chained_model_field='departamentos', on_delete=django.db.models.deletion.CASCADE, to='sitios.ciudades'),
        ),
        migrations.AddField(
            model_name='centros',
            name='departamentos',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='sitios.departamentos'),
        ),

    ]
