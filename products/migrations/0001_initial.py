# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pname', models.CharField(max_length=200)),
                ('pdesc', models.CharField(max_length=200)),
                ('pstatus', models.BooleanField(default=True)),
            ],
        ),
    ]
