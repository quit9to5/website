# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('our_form', '0003_auto_20150621_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='datd',
            new_name='date',
        ),
    ]
