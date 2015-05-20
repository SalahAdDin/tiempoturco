import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.utils.translation import ugettext_lazy as _

from actions import week_range
import datetime

from .models import Documentation


# Mixin
class MenuMixin(object):
    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['docs'] = self.models.objects.all()
        return context


# Create your views here.
class DocumentationView(MenuMixin, DetailView):
    template_name = 'docs_template.html'
    model = Documentation


class DocumentationListView(ListView):
    template_name = ''
    model = Documentation