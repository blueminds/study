# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('numero_horas_total', models.CharField(max_length=10, blank=True)),
                ('numero_horas_semana', models.CharField(max_length=10, blank=True)),
                ('pais', models.CharField(max_length=20, blank=True)),
                ('ciudad', models.CharField(max_length=20, blank=True)),
                ('escuela', models.CharField(max_length=10, blank=True)),
                ('edad_minima', models.CharField(max_length=10, blank=True)),
                ('nivel_ingles_requerido', models.CharField(max_length=10, blank=True)),
                ('opcion_trabajo', models.CharField(max_length=10, blank=True)),
            ],
        ),
    ]
