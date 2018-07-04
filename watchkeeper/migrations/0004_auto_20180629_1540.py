# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchkeeper', '0003_watchkeeper_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchkeeper',
            options={'verbose_name': '\u8fd0\u7ef4\u4eba\u5458', 'verbose_name_plural': '\u8fd0\u7ef4\u4eba\u5458'},
        ),
        migrations.AddField(
            model_name='watchkeeper',
            name='email',
            field=models.EmailField(default=b'', max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='phone',
            field=models.CharField(default=b'', max_length=11, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d'),
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='tag',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\x9c\x80\xe8\xa6\x81\xe5\x80\xbc\xe7\x8f\xad', choices=[(0, b'\xe9\x9c\x80\xe8\xa6\x81'), (1, b'\xe4\xb8\x8d\xe9\x9c\x80\xe8\xa6\x81')]),
        ),
    ]
