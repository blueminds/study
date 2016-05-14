# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0008_reserva_agente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('reserva', models.ForeignKey(blank=True, to='registros.Reserva', null=True)),
            ],
        ),
    ]
