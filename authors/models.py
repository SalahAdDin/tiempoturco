from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import ImageField
from django.utils.translation import ugettext_lazy as _

from django.db import models


# Create your models here.
class AuthorInfo(models.Model):

    # Campos del Usuario
    photo = ImageField(verbose_name=_('Photo'), blank=True, null=True, upload_to='images/authors', )
    user = models.OneToOneField(User, verbose_name=_('User'), )
    biography = models.TextField(verbose_name=_('Biography'), blank=True, null=True, )
    age = models.PositiveIntegerField(verbose_name=_('Age'), blank=True, null=True, )
    link_own = models.URLField(verbose_name=_('Link'), blank=True, null=True, )

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        ordering = ('user__last_name',)

    # def __str__(self):
    #    return '%s %s' % (User.model.first_name,User.model.last_name)

    # No tiene utilidad
    def photo_display(self):
        if self.photo:
            return '<img src="%s" alt="%s" title="%s">' % (get_thumbnail(self.photo, '100x100').url,
                                                           self.first_name, self.first_name)
        else:
            return '/statics/tiempoturco/app/images/no-profile.png'

    # Usuario autor también debe de poder modificar su propio perfil, no otro, y su información personal,
    # no los permisos u otra cosa.

    def get_absolute_url(self):
        return reverse('AuthorInfoView', args=[str(self.user.username)])