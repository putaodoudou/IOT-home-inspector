# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 20:51
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='devices',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('philips-hue', 'Philips Hue'), ('amazon-echo', 'Amazon Echo'), ('nest', 'Nest'), ('fitbit', 'FitBit')], max_length=35),
        ),
    ]
