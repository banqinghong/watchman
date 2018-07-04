# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchkeeper', '0006_auto_20180629_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchlist',
            options={'verbose_name': '\u503c\u73ed\u8868', 'verbose_name_plural': '\u503c\u73ed\u8868'},
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='email',
            field=models.EmailField(default=b'', max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='name',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='phone',
            field=models.CharField(default=b'', max_length=11, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d', blank=True),
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='qq',
            field=models.CharField(default=b'', max_length=13, verbose_name=b'QQ\xe5\x8f\xb7', blank=True),
        ),
    ]
