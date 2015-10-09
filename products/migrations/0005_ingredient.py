# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20151009_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('iname', models.CharField(max_length=200)),
                ('idesc', models.CharField(max_length=200)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
    ]
