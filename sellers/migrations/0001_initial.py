# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchaser_name', models.CharField(help_text='The purchase name.', max_length=50, verbose_name='Purchase name')),
                ('item_description', models.CharField(help_text='Description for the purchased item.', max_length=50, verbose_name='Item description')),
                ('item_price', models.DecimalField(help_text='The price of the purchased item in decimal format.', verbose_name='Item price', max_digits=10, decimal_places=2)),
                ('purchase_count', models.PositiveSmallIntegerField(help_text='Number of items purchased.', verbose_name='Purchase count')),
                ('merchant_address', models.CharField(help_text='The merchant address.', max_length=50, verbose_name='Merchant address')),
                ('merchant_name', models.CharField(help_text='The merchant name.', max_length=50, verbose_name='Perchant name')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
