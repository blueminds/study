# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0007_auto_20160514_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='agente',
            field=models.ForeignKey(blank=True, to='registros.Agente', null=True),
        ),
    ]
