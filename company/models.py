# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
import PIL
import os.path
from energy_vector.settings import BASE_DIR
from django.core.files import File
import os
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from . widgets import PhoneField

# Create your models here.
class Marka(models.Model):
	marka = models.CharField(max_length=10,unique=True)
	

	def __unicode__(self):
		return self.marka


class Certificate(models.Model):
	# marka = models.ForeignKey(Marka, 
	# 	verbose_name = u'Выберите из списка или введите новое название марки:',
	# 	on_delete=models.CASCADE,null=True,default=None,)
	certificate = models.ImageField(u'Выберите файл в формате .jpg или .jpeg',
		upload_to = 'certificates')
	certificate_1x = models.ImageField(null=True,default=None,
		upload_to = 'certificates')
	certificate_2x = models.ImageField(null=True,default=None,
		upload_to = 'certificates')


	def __unicode__(self):
		return self.certificate.name

	def save(self,*args,**kwargs):
		try:
			this_record=Certificate.objects.get(id=self.id)
			if this_record.certificate !=self.certificate:
				this_record.certificate.delete(save=False)
		except:
			pass
		super(Certificate,self).save(*args,**kwargs)

	def delete(self,*args,**kwargs):
		self.certificate.delete(save=False)
		self.certificate_1x.delete(save=False)
		self.certificate_2x.delete(save=False)
		
		super(Certificate,self).delete(*args,**kwargs)

	def certificate_1x_2x(self):
		
		img=PIL.Image.open(self.certificate.path)
		
		size=(((260,355),'_1x'),((582,800),'_2x'),)
		
		# django_like_files - list с двумя Django file-like objects
		django_like_files=[]

		# name - имя загруженного файла-изображения
		name=self.certificate.name

		for item in size:
			# делаем копию нашего исходного PIL объекта:
			foto_copy=img.copy()
			# преобразуе с помощю PIL в нужный формат
			foto_copy.thumbnail(item[0], PIL.Image.ANTIALIAS)

			if name.find('.jpeg')>-1:
				new_name=name.replace('.jpeg',item[1]+'.png')
			elif name.find('.JPEG')>-1:
				new_name=name.replace('.JPEG',item[1]+'.png')
			elif name.find('.jpg')>-1:
				new_name=name.replace('.jpg',item[1]+'.png')
			elif name.find('.JPG')>-1:
				new_name=name.replace('.JPG',item[1]+'.png')
			elif name.find('.png')>-1:
				new_name=name.replace('.png',item[1]+'.png')
			else:
				pass
			# создаем объект StringIO -
			foto_copy_io = StringIO.StringIO()
			# запоминаем в него наш PIlовский foto_copy
			foto_copy.save(foto_copy_io, format='png')

			#  создаем new Django file-like object, чтобы впоследствии запомнить его в 
			# ImageFild поле модели

			foto_copy_file = InMemoryUploadedFile(foto_copy_io, None, new_name, 'image/png',
                                  foto_copy_io.len, None)				

			django_like_files.append(foto_copy_file)
		
		self.certificate_1x=django_like_files[0]
		
		self.certificate_2x=django_like_files[1]
		
class Otziv(models.Model):

	otziv = models.ImageField(u'Выберите файл отзыва в формате .jpg или .jpeg',upload_to = 'otziv',)
	
	otziv_1x = models.ImageField(null=True,default=None,upload_to = 'otziv',)
	
	otziv_2x = models.ImageField(null=True,default=None,upload_to = 'otziv',)

	text = models.TextField(null=True,default=None,blank=True,max_length=1000,)
	

	def __unicode__(self):
		return self.otziv.name

	def save(self,*args,**kwargs):
		try:
			this_record=Otziv.objects.get(id=self.id)
			if this_record.otziv !=self.otziv:
				this_record.otziv.delete(save=False)
		except:
			pass
		super(Otziv,self).save(*args,**kwargs)

	def delete(self,*args,**kwargs):
		self.otziv.delete(save=False)
		self.otziv_1x.delete(save=False)
		self.otziv_2x.delete(save=False)
		
		super(Otziv,self).delete(*args,**kwargs)

	def otziv_1x_2x(self):
		
		img=PIL.Image.open(self.otziv.path)
		
		size=(((260,355),'_1x'),((582,800),'_2x'),)
		
		# django_like_files - list с двумя Django file-like objects
		django_like_files=[]

		# name - имя загруженного файла-изображения
		name=self.otziv.name

		for item in size:
			# делаем копию нашего исходного PIL объекта:
			foto_copy=img.copy()
			# преобразуе с помощю PIL в нужный формат
			foto_copy.thumbnail(item[0], PIL.Image.ANTIALIAS)

			if name.find('.jpeg')>-1:
				new_name=name.replace('.jpeg',item[1]+'.png')
			elif name.find('.JPEG')>-1:
				new_name=name.replace('.JPEG',item[1]+'.png')
			elif name.find('.jpg')>-1:
				new_name=name.replace('.jpg',item[1]+'.png')
			elif name.find('.JPG')>-1:
				new_name=name.replace('.JPG',item[1]+'.png')
			elif name.find('.png')>-1:
				new_name=name.replace('.png',item[1]+'.png')
			else:
				pass
			# создаем объект StringIO -
			foto_copy_io = StringIO.StringIO()
			# запоминаем в него наш PIlовский foto_copy
			foto_copy.save(foto_copy_io, format='png')

			#  создаем new Django file-like object, чтобы впоследствии запомнить его в 
			# ImageFild поле модели

			foto_copy_file = InMemoryUploadedFile(foto_copy_io, None, new_name, 'image/png',
                                  foto_copy_io.len, None)				

			django_like_files.append(foto_copy_file)
		
		self.otziv_1x=django_like_files[0]
		
		self.otziv_2x=django_like_files[1]	

class Callorderuser(models.Model):

	name = models.CharField(u'ИМЯ',max_length=20,) 
	phone = PhoneField(code_length = 3, num_length = 7)
	text = models.CharField(u'ВОПРОС',max_length=200,)

	published_date = models.DateField()

	

		


