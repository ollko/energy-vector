# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from precise_bbcode.fields import BBCodeTextField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from markdown_deux import markdown


class New(models.Model):
    title = models.CharField(max_length = 100,
        unique_for_date = 'publish',
        verbose_name = "Заголовок"
    )   
    image = ProcessedImageField(verbose_name = 'Картинка',
        help_text = "Будет лучше загрузить landscape фото ",
        upload_to='new_image',
        processors= [ResizeToFill(750,500)],
        format='JPEG',
        options={'quality': 60},
        blank = True,
        null = True,
    )
    content = models.TextField('Содержание')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, blank = True, null = True, default = None)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    # is_commentable = models.BooleanField(default = True, verbose_name = "Разрешены комментарии")
    # tags = TaggableManager(blank = True, verbose_name = "Теги")
    # user = models.ForeinKey(User, editable = False)


    class Meta:
        ordering = ["-timestamp", "-updated"]
        verbose_name = "Новостная статья"
        verbose_name_plural = "Новостные статьи"


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("news:news_detail", kwargs = {'pk': self.pk})


    def get_markdown(self):
        content = self.content
        markdown_content = markdown(content)
        return mark_safe(markdown_content)


    def delete(self, *args, **kwargs):
        self.image.delete(save = False)
        super(New, self).delete(*args, **kwargs)


# from django.contrib.comments.moderation import CommentModerator, moderator

# class NewsModerator(CommentModerator):
#   email_notification = True
#   enable_field = 'is_commentable'
    
# moderator.register(News,NewsModerator)


        
