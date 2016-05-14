# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_auto_20160514_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50, blank=True)),
                ('apellidos', models.CharField(max_length=50, blank=True)),
                ('numero_pasaporte', models.TextField(max_length=50, blank=True)),
                ('correo', models.CharField(max_length=50, blank=True)),
                ('numero_identificacion', models.CharField(max_length=50, blank=True)),
                ('numero_telefono', models.CharField(max_length=50, blank=True)),
                ('pais', models.CharField(max_length=50, blank=True)),
                ('ciudad', models.CharField(max_length=50, blank=True)),
                ('direccion', models.CharField(max_length=50, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='numero_pasaporte',
            field=models.TextField(max_length=50, blank=True),
        ),
    ]
