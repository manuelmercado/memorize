# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('date_tarea', models.DateTimeField(auto_now=True)),
                ('state', models.BooleanField()),
                ('owner', models.ForeignKey(to='usuario.Usuarios')),
            ],
        ),
    ]
