from django.core.mail import send_mail, mail_admins
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from smart_selects.db_fields import ChainedForeignKey

from tags.models import KeyWord, Topic, Subtopic


# Create your models here.

class New(models.Model):
    author = models.ForeignKey(User, verbose_name=_('Author'), related_name='news')
    content = RichTextField(verbose_name=_('Content'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Datetime'))
    is_published = models.BooleanField(verbose_name=_('Published'), default=False, )
    keywords = models.ManyToManyField(KeyWord, blank=True, verbose_name=_('Keywords'), related_name='news',
                                      help_text=_('Tags related with this new!'), )
    place = models.CharField(max_length=255, verbose_name=_('Place'),
                             help_text=_('Place in which the new happened. Normally is a city!'), )
    source = models.URLField(verbose_name=_('Source'),
                             blank=True, help_text=_('Source of the new, for example, a web page.'), )
    times_viewed = models.PositiveIntegerField(default=0, editable=False, verbose_name=_('Times viewed'))
    title = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, unique=True,
                            help_text=_("Put a title's copy as slug automatically!"), )
    topic = models.ForeignKey(Topic, verbose_name=_('Topic'), related_name='news', )
    subtopic = ChainedForeignKey(
        Subtopic, chained_field='topic', chained_model_field='topic', show_all=False, auto_choose=True,
        verbose_name=_('Subtopic'), related_name='news',
    )

    class Meta:
        verbose_name = _('New')
        verbose_name_plural = _('News')
        ordering = ('-created_date',)

        permissions = (
            ("can_publish", "Puede publicar noticias"),  # Can publish news
        )

    def first_image(self):
        return self.images.first()  # Siendo images el related_name en Image

    def get_all_images(self):
        return self.images.all()

    def get_video(self):
        return self.videos  # Devuelve el video de la Noticia

    def get_absolute_url(self):
        return reverse('NewsDefaultView',
                       args=[str(self.created_date.strftime("%Y")), str(self.created_date.strftime("%m")),
                             str(self.created_date.strftime("%d")), str(self.slug)])

    def get_all_keys(self):
        keys_list = self.keywords.values_list('name', flat=True)
        return str(keys_list).strip("'[]'").replace("'", '')

    # def is_published(self): devuelve si la noticia ha sido pulicada para que salga en la lista de noticias

    def __str__(self):
        return self.title

    def save(self):  # Definir metodo para guardar, validar y otros metodos del Slug
        super(New, self).save()  # Solo con este me funciona correctamente
        if not self.id:
            self.slug = slugify(self.title)
        super(New, self).save()


from django.db.models.signals import post_save
from django.template.loader import get_template
from django.template import Context

# admin = User.objects.get(is_superuser=True).get_full_name()


def send_created_notification(instance, created, ):
    admin = User.objects.get(is_superuser=True).get_full_name()
    # Bueno, hay dos problemas aquí,
    # aquí obtenemos el nombre directamente, luego, a que superusiarios enviará el mail?
    # Ordenamos alfabéticamente?  le enviamos un user personalizado y creamos un mètodo que haga esta misma opción?
    # Creo que esto lo puede hacer con x número de destinatarios, el problema es que el correo llegue con el nombre del
    # destinatario
    if created:
        return mail_admins(_('A new story are waiting to be edited!'), get_template('email_new_news_template.txt').render(
            Context({
                'user': admin,
                'author': instance.author,
                'title': instance.title,
                'date': instance.created_date
            })
        ),
            html_message=get_template('email_new_news_template.html').render(
            Context({
                'user': admin,
                'author': instance.author,
                'title': instance.title,
                'date': instance.created_date
                })
            ))
    else:
        pass


# post_save.connect(send_created_notification, sender=New) #Reactivar en servidor


def send_published_notification(instance):
    if instance.is_published:
        return send_mail(_('Your new was published!'), get_template('email_publish_news_template.txt').render(
            Context({
                'author': instance.author,
                'title': instance.title,
                'date': instance.created_date
            })
        ),
            'oficial@tiempoturco.com', [instance.author.email],
            html_message=get_template('email_publish_news_template.html').render(
            Context({
                'author': instance.author,
                'title': instance.title,
                'date': instance.created_date
            })
        ))
    else:
        pass

# post_save.connect(send_published_notification, sender=New)


from permission import add_permission_logic
from permission.logics import AuthorPermissionLogic, StaffPermissionLogic

add_permission_logic(New, AuthorPermissionLogic(
    field_name='author',
    any_permission=False,
    change_permission=True,
    delete_permission=True,
))
add_permission_logic(New, StaffPermissionLogic(
    any_permission=False,
    change_permission=True,
    delete_permission=True,
))

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.sessions.models import Session


@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()