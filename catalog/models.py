# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gensetengine(models.Model):
	engine = models.CharField(max_length = 20, unique = True,
			verbose_name = "Производитель двигателя ДГУ")
	logo = models.ImageField(verbose_name = "Логотип", 
			upload_to = 'catalog/dgu/logo', blank=True, null=True, default=None,)

	text = models.TextField(verbose_name = 'Текст, кот. будет выводиться перед ...',
			blank=True, null=True, default=None,)

	def __unicode__(self):
		return self.engine

	def save(self,*args,**kwargs):
		try:
			this_record=Gensetengine.logo.get(id=self.id)
			if this_record.logo !=self.logo:
				this_record.logo.delete(save=False)
		except:
			pass
		super(Gensetengine,self).save(*args,**kwargs)

	def delete(self,*args,**kwargs):
		self.logo.delete(save=False)		
		super(Gensetengine,self).delete(*args,**kwargs)

class Genset(models.Model):
	gensetengine = models.ForeignKey(Gensetengine,verbose_name = 'Марка двигателя')
	model = models.CharField(verbose_name = "Марка  дизельгенератора",
				max_length = 10, unique = True)
	stand_by_kva = models.DecimalField(verbose_name = "ESP(Stand-by)/кВА", max_digits=4, decimal_places=1)
	stand_by_kw = models.DecimalField(verbose_name = "ESP(Stand-by)/кВт", max_digits=4, decimal_places=1)
	prime_kva = models.DecimalField(verbose_name = "PRP(Prime)/кВА", max_digits=4, decimal_places=1)
	prime_kw = models.DecimalField(verbose_name = "PRP(Prime)/кВт", max_digits=4, decimal_places=1)
	
	engine_model = models.SlugField(verbose_name = "Модель двигателя", max_length = 20, unique = True)

	spec = models.FileField(verbose_name = "pdf файл спецификации",
		upload_to = 'catalog/dgu/spec_pdf', blank=True, null=True, default=None,)

	def __unicode__(self):
		return self.model

	def save(self,*args,**kwargs):
		try:
			this_record=Gensetspec.get(id=self.id)
			if this_record.spec !=self.spec:
				this_record.spec.delete(save=False)
		except:
			pass
		super(Genset,self).save(*args,**kwargs)

	def delete(self,*args,**kwargs):
		self.spec.delete(save=False)		
		super(Genset,self).delete(*args,**kwargs)