# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('ubicacion_maps', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='escuela',
        ),
        migrations.AddField(
            model_name='escuela',
            name='curso',
            field=models.ForeignKey(blank=True, to='registros.Curso', null=True),
        ),
    ]
