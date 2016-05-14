# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_auto_20160514_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('curso', models.ForeignKey(blank=True, to='registros.Curso', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50, blank=True)),
                ('apellidos', models.CharField(max_length=50, blank=True)),
                ('correo', models.CharField(max_length=50, blank=True)),
                ('numero_identificacion', models.CharField(max_length=50, blank=True)),
                ('numero_telefono', models.CharField(max_length=50, blank=True)),
                ('pais', models.CharField(max_length=50, blank=True)),
                ('ciudad', models.CharField(max_length=50, blank=True)),
                ('direccion', models.CharField(max_length=50, blank=True)),
            ],
        ),
    ]
