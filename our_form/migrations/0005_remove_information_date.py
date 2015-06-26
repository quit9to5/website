# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('our_form', '0004_auto_20150621_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='date',
        ),
    ]
