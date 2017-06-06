# coding=utf-8
from django import forms

from .widgets import MultiFileInput, PhoneField
from .models import Callorderuser,Marka
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User



class CertificateForm(forms.Form):

	# def get_choice_marka_list():
	# 	'''
	# 	возвращает список кортежиков типа [(1,марка1),(2,марка2)...]
	# 	'''
	# 	m = Marka.objects.all()
	# 	l=[]
	# 	for i in m:
	# 		l.append(i.marka)
	# 	choice_list= [ i for i in l ]
	# 	print 'choice_list=',choice_list
	# 	return choice_list		
    
	# # marka = forms.CharField(label=u'марка оборудования', max_length=20)
	# marka_choice_fild = forms.ChoiceField(widget = forms.Select(), 
 #                 choices = (get_choice_marka_list()), )
	# marka_new = forms.CharField(label=u'ВЫБЕРИТЕ МАРКУ СЕРТИФИКАТА', max_length = 20,)
	# class Meta:
	# 	model = Marka
	# 	fields = ('marka')

	certificate = forms.ImageField(label=u'', widget = MultiFileInput)
	

	
# class RegistrationForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ('first_name','last_name','email')

class OtzivForm(forms.Form):
	
	otziv = forms.ImageField(label=u'',)
	text = forms.CharField(label=u'наберите кратко текст отзыва:',
				 max_length = 1000,widget = forms.widgets.Textarea)
			
class Callorder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ',max_length = 20)

	phone_number=PhoneField(label = u'НОМЕР ТЕЛЕФОНА',code_length = 3, num_length = 7)

	question = forms.CharField(label=u'ВОПРОС',max_length = 1000, widget = forms.widgets.Textarea)
