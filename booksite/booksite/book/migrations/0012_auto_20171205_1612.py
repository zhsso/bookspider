# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-05 08:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20171205_1611'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('book_number', 'site')]),
        ),
    ]
