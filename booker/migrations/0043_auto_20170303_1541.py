# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0042_auto_20170303_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectionlist',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='arrangement', serialize=False, to='booker.Event'),
        ),
    ]
