# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serveur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('h_datcre', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('h_datmod', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
                ('statut', models.BooleanField(default=True, verbose_name='Actif')),
                ('S_Nom', models.CharField(max_length=30, verbose_name='Nom')),
                ('S_Type', models.CharField(default='PHY', choices=[('VM', 'Machine Virtuelle'), ('PHY', 'Physique')], max_length=3, verbose_name='Type')),
                ('S_IP', models.GenericIPAddressField(default='127.0.0.1', verbose_name='Adr IP')),
                ('S_OSTYPE', models.CharField(default='UNIX', choices=[('UNIX', 'UNIX'), ('WIN', 'WINDOWS'), ('AUT', 'AUTRES')], max_length=5, verbose_name='Famille OS')),
                ('S_OSVersion', models.CharField(blank=True, max_length=30, verbose_name='OS Version')),
                ('S_Desc', models.TextField(blank=True, default=' ', verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
