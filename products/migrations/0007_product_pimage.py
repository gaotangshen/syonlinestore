# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20151010_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.FileField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
