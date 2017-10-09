# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-09 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=20, verbose_name='谁的消息')),
                ('content', models.CharField(max_length=30, verbose_name='消息内容')),
                ('link', models.CharField(max_length=50, verbose_name='链接')),
                ('status', models.IntegerField(choices=[(-1, '未读'), (0, '删除'), (1, '已读')], verbose_name='状态')),
            ],
            options={
                'verbose_name': '未读的站内信',
                'verbose_name_plural': '未读的站内信',
            },
        ),
    ]
