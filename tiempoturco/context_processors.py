from random import choice
from django.contrib.sites.models import Site


def basic(request):
    return {
        'meta_contentsf': 'Portal de Noticias de Turquía en Español para Latino América, '
                          'para el mundo de habla Hispana. Manténgase de lo que pasa en Turquía, ahora en su idioma.',
        'meta_contentss': 'Turquía, Noticias en Español, LatinoAmérica, Noticias de Turquía',
        'meta_author': 'Barakat Studios',
        'meta_today_title': 'Noticias de hoy en Tiempo Turco',
        'meta_today_des': 'Noticias publicadas hoy en Tiempo Turco',
        'meta_today_keys': 'hoy, tiempo turco, últimas, noticias, actualidad, actuales',
        'site': Site.objects.get_current(),
        }