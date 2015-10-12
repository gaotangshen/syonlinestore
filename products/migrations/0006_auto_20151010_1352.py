# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='idesc',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='pdesc',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
