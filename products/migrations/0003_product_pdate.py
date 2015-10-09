# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20151009_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdate',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True, verbose_name='add date'),
        ),
    ]
