from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from embed_video.admin import AdminVideoMixin
from import_export.admin import ImportExportModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Gallery, Image, Video

from actions import export_as_excel
# Register your models here.


class ImageInLine(AdminImageMixin, admin.StackedInline):
    fieldsets = [
        (None, {
            'fields': ['name', 'slug', ]}),
        (None, {
            'fields': ['image', 'caption', ]}),
        (None, {
            'fields': ['gallery', 'news', ]}),
    ]
    model = Image

    prepopulated_fields = {"slug": ("name",)}
    suit_classes = 'suit-tab suit-tab-images'


class VideoInLine(AdminVideoMixin, admin.StackedInline):
    fieldsets = [
        (None, {
            'fields': ['name', 'slug', ]}),
        (None, {
            'fields': ['video', 'caption', ]}),
        (None, {
            'fields': ['gallery', 'news', ]}),
    ]
    model = Video

    prepopulated_fields = {"slug": ("name",)}
    suit_classes = 'suit-tab suit-tab-videos'


class GalleryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = (export_as_excel,)

    fieldsets = [
        (_('Title'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': _("Gallery's Name"),
            'fields': ['name', 'slug', ]}),
        (_('Information'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': _("Gallery's Information"),
            'fields': ['caption', 'news', ]}),
    ]

    inlines = [ImageInLine, VideoInLine, ]
    list_display = ('id', 'name', 'caption', 'author', 'image_counter', 'created_date', 'times_viewed', )
    list_editable = ('name', 'author', )
    list_filter = ('author__first_name', 'author__last_name', 'created_date', 'times_viewed', )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('author__first_name', 'author__last_name', 'times_viewed', )
    suit_form_tabs = (('general', _('General')), ('images', _('Images')), ('videos', _('Videos')))

    def image_counter(self, obj):
        # Imprime en pantalla el numero de noticias del autor
        return obj.images.all().count()
    image_counter.short_description = _('Image')
    image_counter.allow_tags = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Gallery, GalleryAdmin)


class ImageAdmin(ImportExportModelAdmin, AdminImageMixin, admin.ModelAdmin):
    fieldsets = [
        (_('Title'), {
            'fields': ['name', 'slug', ]}),
        (_('Content'), {
            'fields': ['image', 'caption', ]}),
        (_('Information'), {
            'fields': ['gallery', 'news', 'docs', ]}),
    ]
    list_display = ('id', 'name', 'caption', 'image', 'news', 'created_date', 'times_viewed', )
    list_filter = ('name', 'id', 'created_date', )
    list_editable = ('name', 'caption', 'image', )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'news__title', 'news__author', 'times_viewed', )

    # def image_view(self, obj):
    #        return '<img src="%s" alt="%s" title="%s">' % (get_thumbnail(obj.image, '100x100').url, obj.name, obj.name)
    # image_view.short_description = 'Imagen'
    # image_view.allow_tags = True

admin.site.register(Image, ImageAdmin)


class VideoAdmin(ImportExportModelAdmin, AdminVideoMixin, admin.ModelAdmin):
    fieldsets = [
        (_('Title'), {
            'fields': ['name', 'slug', ]}),
        (_('Content'), {
            'fields': ['video', 'caption', ]}),
        (_('Information'), {
            'fields': ['gallery', 'news', 'docs', ]}),
    ]
    list_display = ('id', 'name', 'caption', 'video_view', 'news', 'created_date', 'times_viewed', )
    list_filter = ('name', 'id', 'created_date', )
    list_editable = ('name', 'caption')
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ('news', )
    search_fields = ('name', 'news__title', 'news__author', 'times_viewed', )

    def video_view(self, obj):
        return render_to_string('thumb.html', {'video': obj.video})

    video_view.short_description = _('Video')
    video_view.allow_tags = True

admin.site.register(Video, VideoAdmin)