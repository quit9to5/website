# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('our_form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='addredd_text',
            new_name='address_text',
        ),
    ]
