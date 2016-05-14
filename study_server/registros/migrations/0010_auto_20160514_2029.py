# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0009_pago'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actividades',
            new_name='Actividad',
        ),
    ]
