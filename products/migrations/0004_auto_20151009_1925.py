# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_pdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pdate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='add date'),
        ),
    ]
