from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from embed_video.admin import AdminVideoMixin
from sorl.thumbnail.admin import AdminImageMixin
from import_export.admin import ImportExportModelAdmin

from .models import New
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


class NewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = ['make_publish', 'make_unpublish', 'export_as_excel', ]

    fieldsets = [
        (_('Title'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title', 'slug', 'is_published', ]}),
        (_('Content'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['content', ]}),
        (_('Information'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['topic', 'subtopic', 'place', 'source', 'keywords', ]}),
    ]

    inlines = [ImageInLine, VideoInLine, ]
    filter_horizontal = ('keywords',)
    list_display = ('author', 'title', 'topic', 'subtopic', 'is_published', 'times_viewed', 'created_date',)
    list_filter = ('author', 'title', 'topic', 'subtopic', 'is_published', 'times_viewed', 'created_date',)
    list_editable = ('title', 'topic', 'subtopic',)
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('author', )
    search_fields = ('author__first_name', 'author__last_name', 'title', 'topic__name', 'subtopic__name',
                     'created_date', 'is_published', 'times_viewed')
    # Si quiero buscar noticias por el apellido de su author 'author__last_name'
    suit_form_tabs = (('general', _('General')), ('images', _('Images')), ('videos', _('Videos')))

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(NewAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def get_actions(self, request):
        actions = super(NewAdmin, self).get_actions(request)
        if request.user.groups.filter(name="Author"): 
            if 'make_publish' in actions:
                del actions['make_publish']
            if 'make_unpublish' in actions:
                del actions['make_unpublish']
        return actions
    
    def get_queryset(self, request):
        # queryset = super(New, self).get_queryset(request)
        if request.user.groups.filter(name="Author"):  # is the user an author?
            # queryset = queryset.filter(author=self.user)  # only allow users to edit their own posts
            # print(request.user.groups.filter(name="Author"))
            return New.objects.filter(author=request.user)
        return New.objects.all()

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(NewAdmin, self).get_readonly_fields(request, obj)
        if request.user.groups.filter(name="Author"):  # is the user an author?
            readonly_fields = ['is_published']  # don't allow authors to change the publish status
            return readonly_fields
        return readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:  # getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
        
    # Actions
    def make_publish(self, request, queryset):
        rows_published = queryset.update(is_published=True)
        if rows_published == 1:
            message_bit = _('1 new was')
        else:
            message_bit = _('%s news were') % rows_published
        self.message_user(request, _('%s successfully published.') % message_bit)

    make_publish.short_description = _('Publish New')

    def make_unpublish(self, request, queryset):
        rows_unpublished = queryset.update(is_published=False)
        if rows_unpublished == 1:
            message_bit = _('1 new was')
        else:
            message_bit = _('%s news were') % rows_unpublished
        self.message_user(request, _('%s successfully published.') % message_bit)

    make_unpublish.short_description = _('Un-publish New')    

admin.site.register(New, NewAdmin)
