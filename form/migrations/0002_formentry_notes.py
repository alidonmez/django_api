# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-11 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formentry',
            name='notes',
            field=models.TextField(default='', max_length=255),
        ),
    ]
