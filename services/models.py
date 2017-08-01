# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from precise_bbcode.fields import BBCodeTextField

LINKS = (('/call_order/', 'ЗАКАЗАТЬ ЗВОНОК'),
		('/order/maintenance/dgu/', 'ЗАКАЗАТЬ ТЕХОБСЛУЖИВАНИЕ ДГУ'),
		('/order/maintenance/ups/', 'ЗАКАЗАТЬ ТЕХОБСЛУЖИВАНИЕ ИБП'),
		('/order/repair/dgu/','ЗАКАЗАТЬ РЕМОНТ ДГУ'),
		('/order/repair/ups/','ЗАКАЗАТЬ РЕМОНТ ИБП'),)
# Create your models here.
class Service(models.Model):
	serv_name = models.CharField(verbose_name = 'УСЛУГА', max_length=80, unique = True,)
	content = BBCodeTextField(verbose_name = 'ТЕКСТ ДЛЯ СТРАНИЦЫ УСЛУГИ',
								blank=True, null=True, default=None,)

	link = models.CharField(verbose_name = 'ЕСЛИ НУЖНО, ВЫБЕРИТЕ КНОПКУ НА ЗАКАЗ УСЛУГИ', max_length=30, 
								 blank=True, choices = LINKS,)
	

	def __unicode__(self):
		return self.serv_name

	def get_absolute_url(self):
		return u'/services/%d' % self.id 