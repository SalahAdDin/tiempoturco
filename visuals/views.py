from django.shortcuts import render
from django.views.generic import DetailView, ListView, DateDetailView, MonthArchiveView, WeekArchiveView
import datetime

from .models import Gallery, Video, Image
from news.models import New


# Create your views here.
# Mixin
class MenuMixin(object):
    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['latest'] = New.objects.filter(is_published=True).all()[:20]
        context['local'] = New.objects.filter(is_published=True).filter(subtopic__slug='local')[:20]
        context['featured'] = New.objects.order_by('-times_viewed').filter(is_published=True).filter(created_date__year=today.year).filter(created_date__month=today.month)[:20]
        context['images'] = Image.objects.order_by('-created_date').filter(gallery__isnull=True)[:10]
        context['videos'] = Video.objects.order_by('-created_date')[:10]
        # context['gallerys'] = self.model.objects.order_by('-created_date')[:20]
        context['gallerys'] = Gallery.objects.order_by('-created_date')[:20]
        return context


# Vista principal de Galeria
class GalleryDefaultView(MenuMixin, DetailView):
    template_name = 'gallery_template.html'
    model = Gallery

    def get(self, request, *args, **kwargs):
        a = self.get_object()
        if not request.session.get(str(a.id)):
            a.times_viewed += 1
            a.save()
            request.session[a.id] = True

        return super(GalleryDefaultView, self).get(self, request, *args, **kwargs)
        # No es necesario un queryset que filtre solo imagenes sin galeria,
        # ya que solo apareceran en el menu las que no tienen galeria


# Indice de Galerias
class GalleryIndexView(MenuMixin, ListView):
    template_name = 'gallery_index_template.html'
    model = Gallery
    paginate_by = 10


# Vista principal Imagen
class ImageDefaultView(MenuMixin, DetailView):
    template_name = 'image_template.html'
    model = Image

    def get(self, request, *args, **kwargs):
        a = self.get_object()
        if not request.session.get(str(a.id)):
            a.times_viewed += 1
            a.save()
            request.session[a.id] = True

        return super(ImageDefaultView, self).get(self, request, *args, **kwargs)
        # No es necesario un queryset que filtre solo imagenes sin galeria,
        # ya que solo apareceran en el menu las que no tienen galeria


# Indice de Imagenez
class ImageIndexView(MenuMixin, ListView):
    template_name = 'image_index_template.html'
    model = Image
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(gallery__isnull=True)[:10]


# Vista principal Video
class VideoDefaultView(MenuMixin, DetailView):
    template_name = 'video_template.html'
    model = Video

    def get(self, request, *args, **kwargs):
        a = self.get_object()
        if not request.session.get(str(a.id)):
            a.times_viewed += 1
            a.save()
            request.session[a.id] = True

        return super(VideoDefaultView, self).get(self, request, *args, **kwargs)


# Indice de Videos
class VideoIndexView(MenuMixin, ListView):
    template_name = 'video_index_template.html'
    model = Video
    paginate_by = 5