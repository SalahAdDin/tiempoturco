from suit.apps import DjangoSuitConfig
from django.contrib.sites.models import Site


class ZamanDjangoSuitConfig(DjangoSuitConfig):

    admin_name = Site.objects.get_current().name
    menu_position = 'vertical'
    list_per_page = 25
    list_filters_position = 'top'