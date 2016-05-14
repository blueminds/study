# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0005_comentario_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_visa', models.CharField(max_length=50, blank=True)),
                ('seguro', models.CharField(max_length=50, blank=True)),
                ('traslado_areopuerto', models.CharField(max_length=50, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('alojamiento', models.ForeignKey(blank=True, to='registros.Alojamiento', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='actividades',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 14, 19, 58, 51, 997081, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 14, 19, 59, 0, 487542, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 14, 19, 59, 8, 99174, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escuela',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 14, 19, 59, 13, 650946, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 14, 19, 59, 21, 790409, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='curso',
            field=models.ForeignKey(blank=True, to='registros.Curso', null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='estudiante',
            field=models.ForeignKey(blank=True, to='registros.Estudiante', null=True),
        ),
    ]
