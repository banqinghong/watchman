# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchkeeper', '0002_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchkeeper',
            name='phone',
            field=models.CharField(default=b'', max_length=11),
        ),
    ]
