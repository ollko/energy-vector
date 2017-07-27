# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from precise_bbcode.fields import BBCodeTextField

LINKS = (('/call_order/', 'ЗАКАЗАТЬ ЗВОНОК'),
		# ('/maintenance_order_dgu/', 'ЗАКАЗАТЬ ТЕХОБСЛУЖИВАНИЕ ДГУ'),
		# ('/maintenance_order_ups/', 'ЗАКАЗАТЬ ТЕХОБСЛУЖИВАНИЕ ИБП'),
		# ('/repair_order_dgu/','ЗАКАЗАТЬ РЕМОНТ ДГУ'),
		# ('/repair_order_ups/','ЗАКАЗАТЬ РЕМОНТ ИБП'),
		('/order/maintenance/dgu/', 'ЗАКАЗАТЬ ТЕХОБСЛУЖИВАНИЕ ДГУ'),
		('/order/maintenance/ups/', 'ЗАКАЗАТЬ ТЕХОБСЛУЖИВАНИЕ ИБП'),
		('/order/repair/dgu/','ЗАКАЗАТЬ РЕМОНТ ДГУ'),
		('/order/repair/ups/','ЗАКАЗАТЬ РЕМОНТ ИБП'),)
# Create your models here.
class Service(models.Model):
	name = models.CharField(verbose_name = 'УСЛУГА', max_length=80, unique = True,)
	text = BBCodeTextField(verbose_name = 'ТЕКСТ ДЛЯ СТРАНИЦЫ УСЛУГИ',
								max_length=2000, blank=True, null=True, default=None,)

	link = models.CharField(verbose_name = 'ЕСЛИ НУЖНО, ВЫБЕРИТЕ КНОПКУ НА ЗАКАЗ УСЛУГИ', max_length=30, 
								 blank=True, choices = LINKS,)
	

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return u'/services/%d' % self.id 