# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('event_type', models.TextField()),
                ('description', models.TextField()),
                ('dosage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('generic_name', models.CharField(max_length=128)),
                ('brand_names', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='medication',
            name='user',
            field=models.ForeignKey(to='med_tracker_app.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='medication',
            field=models.ForeignKey(to='med_tracker_app.Medication'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to='med_tracker_app.User'),
        ),
    ]
