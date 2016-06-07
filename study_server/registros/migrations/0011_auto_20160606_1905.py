# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0010_auto_20160514_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agente',
            name='numero_pasaporte',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='numero_pasaporte',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
