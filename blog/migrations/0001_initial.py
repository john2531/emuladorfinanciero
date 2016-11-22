# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conceptos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concepto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contabilidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observacion', models.TextField()),
                ('fecha_movimiento', models.DateTimeField(auto_now_add=True)),
                ('entrada', models.IntegerField(null=True, blank=True)),
                ('salida', models.IntegerField(null=True, blank=True)),
                ('saldo_general', models.IntegerField(null=True, blank=True)),
                ('idconcepto', models.ForeignKey(to='blog.Conceptos')),
            ],
        ),
    ]
