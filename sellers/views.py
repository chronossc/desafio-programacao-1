# -*- coding: UTF-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.http import HttpResponseRedirect
from django.views.generic import FormView
from tempfile import mkstemp

from .forms import UploadFileForm
from .importer import Importer1, TabReader
from .models import Sale


def handle_uploaded_file(f, fname):
    with open(fname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class UploadView(FormView):
    form_class = UploadFileForm
    template_name = 'sellers/base.html'

    def form_valid(self, form):
        f = self.request.FILES['file']

        oshandle, fname = mkstemp()

        handle_uploaded_file(f, fname)

        importer = Importer1(fname, reader=TabReader)
        objs = []
        # TODO: importers can validate each field too, like forms
        for result in importer.save_all_iter():
            if result:
                result.pop('_i')
                obj = Sale.objects.create(**result)
                objs.append(obj)

        self.new_objects = objs

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        url = self.request.path

        if getattr(self, 'new_objects'):
            ids = []
            for obj in self.new_objects:
                obj.refresh_from_db()
                ids.append(obj.id)

        return "{}?ids={}".format(
            url,
            ','.join(map(str, ids))
        )

    def get_context_data(self, **context):
        context = super(UploadView, self).get_context_data(**context)
        if self.request.GET.get('ids'):
            # TODO: validate date
            objects = Sale.objects.filter(
                    id__in=self.request.GET.get('ids').split(',')
                )
            context['objects'] = objects
            context['obj_headers'] = \
                dict(([(f.name, f.verbose_name) for f in Sale._meta.fields]))
            context['revenue'] = 0
            for d in objects.values('item_price', 'purchase_count'):
                context['revenue'] += d['item_price'] * d['purchase_count']
        return context
