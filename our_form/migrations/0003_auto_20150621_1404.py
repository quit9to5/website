# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('our_form', '0002_auto_20150621_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='address_text',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='pub_date',
            new_name='datd',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='name_text',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='information',
            old_name='phone_text',
            new_name='phone',
        ),
    ]
