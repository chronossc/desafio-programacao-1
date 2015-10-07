# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class Sale(models.Model):
    purchaser_name = models.CharField(
        max_length=50,
        verbose_name=_("Purchase name"),
        help_text=_("The purchase name.")
    )
    item_description = models.CharField(
        max_length=50,
        verbose_name=_("Item description"),
        help_text=_("Description for the purchased item.")
    )
    item_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name=_("Item price"),
        help_text=_("The price of the purchased item in decimal format.")
    )
    purchase_count = models.PositiveSmallIntegerField(
        verbose_name=_("Purchase count"),
        help_text=_("Number of items purchased.")
    )
    merchant_address = models.CharField(
        max_length=50,
        verbose_name=_("Merchant address"),
        help_text=_("The merchant address.")
    )
    merchant_name = models.CharField(
        max_length=50,
        verbose_name=_("Perchant name"),
        help_text=_("The merchant name.")
    )
    created_time = models.DateTimeField(auto_now_add=True)
