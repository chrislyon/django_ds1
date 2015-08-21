# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('h_datcre', models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')),
                ('h_datmod', models.DateTimeField(auto_now=True, verbose_name='Date de Modification')),
                ('statut', models.BooleanField(verbose_name='Actif', default=True)),
                ('DS_Type', models.CharField(verbose_name='Type', default='ASS', choices=[('ASS', 'Assistance'), ('DEP', 'Depannage'), ('AUD', 'Audit'), ('DEV', 'Developpement'), ('DIV', 'Autres')], max_length=5)),
                ('DS_TiersDemandeur', models.CharField(verbose_name='Demandeur', blank=True, max_length=20)),
                ('DS_TiersFacture', models.CharField(verbose_name='Tiers Facture', default='DEFAUT', blank=True, max_length=20)),
                ('DS_Sujet', models.CharField(verbose_name='Sujet', blank=True, max_length=50)),
                ('DS_Desc', models.TextField(verbose_name='Description', blank=True)),
                ('DS_Statut', models.CharField(verbose_name='Statut', default='NEW', choices=[('NEW', 'Nouvelle'), ('CLOSED', 'Termine'), ('ENC', 'En cours'), ('ATT', 'Attente')], max_length=6)),
                ('DS_Priorite', models.CharField(verbose_name='Priorite', default='N', choices=[('N', 'NORMAL'), ('U', 'URGENT'), ('B', 'BLOQUANT')], max_length=3)),
                ('DS_Assigne', models.CharField(verbose_name='Assigne', blank=True, max_length=30)),
                ('DS_Horo_Debut', models.CharField(verbose_name='Debut', blank=True, max_length=30)),
                ('DS_Horo_Fin', models.CharField(verbose_name='Fin', blank=True, max_length=30)),
                ('DS_Echance', models.CharField(verbose_name='Avant le', blank=True, max_length=30)),
                ('DS_TempsEstime', models.CharField(verbose_name='Temps Estime', blank=True, max_length=30)),
                ('DS_TempsRealise', models.CharField(verbose_name='Temps Realise', blank=True, max_length=30)),
                ('DS_PC_Realise', models.CharField(verbose_name='% Realisation', blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
