# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_conceptos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='fecha_movimiento',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='observacion',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='entrada',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='idconcepto',
            field=models.ForeignKey(default=1, to='blog.Conceptos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='saldo_general',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='salida',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
