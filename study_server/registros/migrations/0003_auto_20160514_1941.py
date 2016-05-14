# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_auto_20160514_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alojamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('costo', models.CharField(max_length=10, blank=True)),
                ('ubicacion', models.CharField(max_length=20, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='escuela',
            name='curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='escuela',
            field=models.ForeignKey(blank=True, to='registros.Escuela', null=True),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='curso',
            field=models.ForeignKey(blank=True, to='registros.Curso', null=True),
        ),
    ]
