# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchkeeper', '0005_auto_20180629_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serverinfo',
            options={'verbose_name': '\u670d\u52a1\u5668', 'verbose_name_plural': '\u670d\u52a1\u5668'},
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='name',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='watchkeeper',
            name='qq',
            field=models.CharField(default=b'', max_length=13, verbose_name=b'QQ\xe5\x8f\xb7'),
        ),
    ]
