# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.conf.urls import url
from .views import UploadView

urlpatterns = (
    url(r'^$', UploadView.as_view(), name='home'),
)

