# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)
import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from sellers.models import Sale
from sellers.importer import Importer1, TabReader


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        importer = Importer1(
            os.path.join(settings.BASE_DIR, 'example_input.tab'),
            reader=TabReader
        )

        for i, result in enumerate(importer.save_all_iter(), 1):
            # result can be False or a dict with row data
            if result is False:
                print("Line %s: Invalid entry." % i)
            else:
                print(result)
