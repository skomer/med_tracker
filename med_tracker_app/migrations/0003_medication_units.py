# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med_tracker_app', '0002_auto_20150810_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='units',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]
