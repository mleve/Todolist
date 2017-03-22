# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-22 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appTodolist', '0003_auto_20170322_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appTodolist.TaskList'),
        ),
    ]
