from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin

from .models import AuthorInfo
from actions import export_as_excel
# Register your models here.


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class AuthorInfoInline(AdminImageMixin, admin.StackedInline):
    model = AuthorInfo
    can_delete = False
    fieldsets = [
        (None, {
            'fields': ['photo', 'age', 'biography', ]}),
        (None, {
            'fields': ['link_own', ]}),
    ]
    verbose_name = _('Profile')
    verbose_name_plural = _('Profiles')


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (AuthorInfoInline, )
    list_display = ('username', 'first_name', 'last_name', 'email',
                    'is_staff', 'news_counter', 'date_joined', 'last_login', )

    def get_fieldsets(self, request, obj=None):
        fsc = super(UserAdmin, self).get_fieldsets(request, obj)
        if not request.user.is_superuser:
            fsc = [
                (None, {
                    'fields': ['username', ]}),
                (_('Personal Information'), {
                    'fields': ['first_name', 'last_name', 'email', ]}),
                (_('Important Dates'), {
                    'fields': ['date_joined', 'last_login', ]}),
            ]
        return fsc

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(UserAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.id:
            return False
        return True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(pk=request.user.id)

    def news_counter(self, obj):
        return obj.news.all().count()
    news_counter.short_description = _('News')
    news_counter.allow_tags = True

# Re-register UserAdmin
# admin.site.register(Permission,) #Desbloquear en servidor
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class AuthorInfoAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = [
        (_('User'), {
            'fields': ['user', ]}),
        ('Bio', {
            'fields': ['photo', 'age', 'biography', ]}),
        (_('Information'), {
            'fields': ['link_own', ]}),
    ]
    list_display = ('id', 'get_user', 'photo', 'age', 'link_own', 'news_counter', )
    list_filter = ('user__first_name', 'user__last_name', )
    search_fields = ('user__first_name', 'user__last_name', )
    # si quiero buscar noticias por el apellido de su author 'author__last_name'
    list_editable = ('age', 'link_own', 'photo', )
    actions = (export_as_excel,)

    def get_user(self, obj):
        return obj.user.get_username()
    get_user.short_description = _('User')
    get_user.allow_tags = True

    def news_counter(self, obj):
        return obj.user.news.all().count()
    news_counter.short_description = _('News')
    news_counter.allow_tags = True

    # Innecesario
    def author_photo(self, obj):
        if obj.photo:
            return '<img src="%s" alt="%s" title="%s">' % \
                   (get_thumbnail(obj.photo, '100x100').url, obj.user.first_name, obj.user.first_name)
        else:
            # obj.photo = '/statics/static/tiempo_turco/images/no-profile.png'
            return '<img src="/statics/tiempoturco/app/images/no-profile.png" ' \
                   'alt="No hay foto de perfil" title="No hay foto de perfil">'
            # return '/statics/static/tiempo_turco/images/no-profile.png'
    author_photo.short_description = _('Photo')
    author_photo.allow_tags = True

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(AuthorInfoAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True

    def get_queryset(self, request):
        if request.user.is_superuser:
            return AuthorInfo.objects.all()
        return AuthorInfo.objects.filter(user=request.user)

admin.site.register(AuthorInfo, AuthorInfoAdmin, )