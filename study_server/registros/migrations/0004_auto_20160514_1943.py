# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_auto_20160514_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('ubicacion', models.CharField(max_length=20, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='Actividades',
            field=models.ManyToManyField(to='registros.Actividades', blank=True),
        ),
    ]
