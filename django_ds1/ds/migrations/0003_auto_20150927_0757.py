# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0002_auto_20150821_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dservice',
            name='DS_Desc',
            field=ckeditor.fields.RichTextField(verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='dservice',
            name='DS_Horo_Debut',
            field=models.DateTimeField(verbose_name='Debut', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='dservice',
            name='DS_Horo_Fin',
            field=models.DateTimeField(verbose_name='Fin', blank=True, max_length=30),
        ),
    ]
