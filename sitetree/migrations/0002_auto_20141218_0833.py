# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treeitem',
            name='css',
            field=models.CharField(default='', max_length=191, blank=True, help_text='Optional css class to associate icons or other styling with the menu item.', verbose_name='Extra CSS', db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treeitem',
            name='isdivider',
            field=models.BooleanField(default=False, help_text='Specifies that this item is a divider, not an link.', verbose_name='Is divider'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='treeitem',
            name='isheader',
            field=models.BooleanField(default=False, help_text='Specifies that this item is a header, not an link.', verbose_name='Is header'),
            preserve_default=True,
        ),
    ]
