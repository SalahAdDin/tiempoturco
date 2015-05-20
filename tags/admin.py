from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from .models import KeyWord, Topic, Subtopic

from actions import export_as_excel

# Register your models here.


class KeyWordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = (export_as_excel,)
    list_display = ('id', 'name', 'slug', 'news_counter', )
    list_editable = ('name', 'slug',)
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name",)}

    def news_counter(self, obj):
        return obj.news.all().count()  # Imprime en pantalla el numero de noticias del autor
    news_counter.short_description = _('News')
    news_counter.allow_tags = True
# Register your models here.

admin.site.register(KeyWord, KeyWordAdmin)


class SubtopicInLine(admin.StackedInline):
    model = Subtopic
    prepopulated_fields = {"slug": ("name",)}


class TopicAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = (export_as_excel,)
    inlines = [SubtopicInLine, ]
    list_display = ('id', 'name', 'slug', 'subtopic_counter', 'news_counter',)
    list_editable = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

    def news_counter(self, obj):
        return obj.news.all().count()
    news_counter.short_description = _('News')
    news_counter.allow_tags = True

    def subtopic_counter(self, obj):
        return obj.subs.all().count()
    subtopic_counter.short_description = _('Subtopics')
    subtopic_counter.allow_tags = True

admin.site.register(Topic, TopicAdmin)


class SubtopicAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    actions = (export_as_excel,)
    list_display = ('id', 'name', 'slug', 'news_counter', )
    list_editable = ('name', 'slug', )
    list_filter = ('topic__name',)
    search_fields = ('topic__name', 'name',)
    prepopulated_fields = {"slug": ("name",)}

    def news_counter(self, obj):
        return obj.news.all().count()  # Imprime en pantalla el numero de noticias del autor
    news_counter.short_description = _('News')
    news_counter.allow_tags = True

admin.site.register(Subtopic, SubtopicAdmin)