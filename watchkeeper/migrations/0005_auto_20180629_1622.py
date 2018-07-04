# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchkeeper', '0004_auto_20180629_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='serverInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name=b'ip\xe5\x9c\xb0\xe5\x9d\x80')),
                ('nickname', models.CharField(max_length=20, verbose_name=b'\xe5\x88\xab\xe5\x90\x8d')),
                ('service', models.TextField(verbose_name=b'\xe8\xbf\x90\xe8\xa1\x8c\xe6\x9c\x8d\xe5\x8a\xa1')),
                ('cpu', models.IntegerField(verbose_name=b'CPU(\xe6\xa0\xb8)')),
                ('mem', models.IntegerField(verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xef\xbc\x88G\xef\xbc\x89')),
                ('system', models.TextField(verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('role', models.CharField(default=b'dev', max_length=20, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\x8e\xaf\xe5\xa2\x83', choices=[(b'dev', b'\xe5\xbc\x80\xe5\x8f\x91\xe7\x8e\xaf\xe5\xa2\x83'), (b'stage', b'stage\xe7\x8e\xaf\xe5\xa2\x83'), (b'lab', b'lab\xe7\x8e\xaf\xe5\xa2\x83'), (b'pd', b'\xe7\x94\x9f\xe4\xba\xa7\xe7\x8e\xaf\xe5\xa2\x83')])),
            ],
            options={
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.AddField(
            model_name='watchkeeper',
            name='qq',
            field=models.CharField(default=b'', max_length=13, verbose_name=b'QQ'),
        ),
    ]
