from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from haystack.forms import FacetedSearchForm, SearchForm
from django.utils.translation import ugettext_lazy as _
from django import forms

from visuals.models import Gallery, Image
from .models import New

# class NewsInlineForm(ModelForm):
#    class Meta:
#        model = New

# ImageFormSet = inlineformset_factory(New,Image)
# GalleryFormSet = inlineformset_factory(New,Gallery)

sort_by = (
    ('', _('No order')),
    ('-created_date', _('Date')),
    ('sorted_name', _('Title')),
    ('-times_viewed', _('As seen')),
)


class DateRangeSearchForm(SearchForm):
    i = forms.DateField(required=False, label='Búsqueda',
                        widget=forms.DateInput(attrs={'type': 'date',
                                                      'class': 'datepicker', 'placeholder': '2014-08-01', }))
    f = forms.DateField(required=False, label='Búsqueda',
                        widget=forms.DateInput(attrs={'type': 'date',
                                                      'class': 'datepicker', 'placeholder': '2016-01-01', }))
    s = forms.ChoiceField(required=False, label='Ordenar por:', widget=forms.Select(), choices=sort_by, )
                        
    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(DateRangeSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        # Check to see if a start_date was chosen.
        if self.cleaned_data['i']:
            sqs = sqs.filter(created_date__gte=self.cleaned_data['i'])
            print(sqs)

        # Check to see if an end_date was chosen.
        if self.cleaned_data['f']:
            sqs = sqs.filter(created_date__lte=self.cleaned_data['f'])

        # Implements sort by
        # sort = self.cleaned_data.get('sort')
        # if sort in sort_by.keys():
        if self.cleaned_data['s']:
            # searchqueryset = searchqueryset.order_by('%s' % sort_by[sort])
            # Existe un error al ordenar por un ChardField
            # print('%s' % self.cleaned_data['s'])
            sqs = sqs.order_by('%s' % self.cleaned_data['s'])
        return sqs


class CustomFacetedSearchForm(DateRangeSearchForm):
    q = forms.CharField(required=False, label='Búsqueda',
                        widget=forms.TextInput(attrs={'type': 'search', 'class': 'gn-search',
                                                      'placeholder': _('Search it and Find it!'), }))

    def __init__(self, *args, **kwargs):
        self.selected_facets = kwargs.pop("selected_facets", [])
        super(CustomFacetedSearchForm, self).__init__(*args, **kwargs)

    def search(self):
        sqs = super(CustomFacetedSearchForm, self).search()

        # We need to process each facet to ensure that the field name and the
        # value are quoted correctly and separately:
        for facet in self.selected_facets:
            if ":" not in facet:
                continue

            field, value = facet.split(":", 1)

            if value:
                sqs = sqs.narrow(u'%s:"%s"' % (field, sqs.query.clean(value)))

        return sqs