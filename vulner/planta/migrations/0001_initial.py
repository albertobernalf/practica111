# Generated by Django 3.2 on 2022-08-01 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilesPlanta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(max_length=30, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='L', max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to='fotos')),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TiposPlanta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('fechaRegistro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('estadoReg', models.CharField(default='A', editable=False, max_length=1)),
            ],
        ),
    ]
