# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0029_event_event_outdoors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('composer', models.CharField(blank=True, max_length=200)),
                ('arrangement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arrangement', to='booker.Ensemble')),
            ],
        ),
    ]