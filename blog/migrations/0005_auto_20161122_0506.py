# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161122_0455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='fecha_movimiento',
            new_name='published_date',
        ),
    ]
