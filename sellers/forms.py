# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django import forms
from django.utils.translation import ugettext as _


class UploadFileForm(forms.Form):
    file = forms.FileField(label=_("Upload a file with tab separated fields."))
