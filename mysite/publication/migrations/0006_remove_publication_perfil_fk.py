# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0005_auto_20170529_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='perfil_fk',
        ),
    ]