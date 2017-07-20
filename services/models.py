# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from precise_bbcode.fields import BBCodeTextField

# Create your models here.
class Service(models.Model):
	name = models.CharField(verbose_name = 'УСЛУГА', max_length=80, unique = True,)
	text = BBCodeTextField(verbose_name = 'ТЕКСТ ДЛЯ СТРАНИЦЫ УСЛУГИ',
								max_length=2000, blank=True, null=True, default=None,)

	link = models.CharField(verbose_name = 'ССЫЛКА НА ОТПРАВКУ ЗАЯВКИ НА УСЛУГУ', max_length=30, 
								 blank=True, default='/send-email/',)
	

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return u'/services/%d' % self.id 