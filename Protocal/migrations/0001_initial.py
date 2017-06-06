# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('AttributeName', models.CharField(max_length=20)),
                ('AttributeType', models.IntegerField()),
                ('AttributeDesc', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'T_Quotation',
            },
        ),
    ]
