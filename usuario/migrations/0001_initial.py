# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('user_pass', models.CharField(max_length=20)),
            ],
        ),
    ]
