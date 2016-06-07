# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0011_auto_20160606_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escuela',
            name='precio',
        ),
        migrations.AddField(
            model_name='curso',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
