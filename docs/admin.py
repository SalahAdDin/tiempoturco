from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from embed_video.admin import AdminVideoMixin
from sorl.thumbnail.admin import AdminImageMixin
from import_export.admin import ImportExportModelAdmin

from .models import Documentation
from visuals.models import Image, Video

from actions import export_as_excel

# Register your models here.


class ImageInLine(AdminImageMixin, admin.StackedInline):
    fieldsets = [
        (None, {
            'fields': ['name', 'slug', ]}),
        (None, {
            'fields': ['image', 'caption', ]}),
        (None, {
            'fields': ['gallery', 'docs', ]}),
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
            'fields': ['gallery', 'docs', ]}),
    ]
    model = Video

    prepopulated_fields = {"slug": ("name",)}
    suit_classes = 'suit-tab suit-tab-videos'


class DocumentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = (export_as_excel, )

    fieldsets = [
        (_('Title'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title', 'slug', ]}),
        (_('Content'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['index', 'content', ]}),
    ]

    inlines = [ImageInLine, VideoInLine, ]
    list_display = ('index', 'author', 'title', 'created_date',)
    list_filter = ('author', 'title', 'created_date',)
    list_editable = ('title', )
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('author', )
    search_fields = ('author__first_name', 'author__last_name', 'created_date', 'index', )
    # si quiero buscar noticias por el apellido de su author 'author__last_name'
    suit_form_tabs = (('general', _('General')), ('images', _('Images')), ('videos', _('Videos')))

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(DocumentationAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if not change:  # getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Documentation, DocumentationAdmin)