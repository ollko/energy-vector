# coding=utf-8
from django import forms

from .widgets import MultiFileInput, PhoneField
from .models import Callorderuser, Marka, Certificate
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

# def validate_images_format(file_instance):

# 	if file_instance.content_type=='image/jpeg':
# 		print 'file_instance.content_type=',file_instance.content_type
		
# 		raise ValidationError("Файл в 'jpeg' формате нельзя загрузить на сайт!")


class CertificateForm(forms.Form):

	certificate = forms.ImageField(label=u'', widget = MultiFileInput,
					# validators = [validate_images_format]
					)

class OtzivForm(forms.Form):
	
	otziv = forms.ImageField(label=u'PDF не поддерживается!',)
	text = forms.CharField(label=u'НАБЕРИТЕ КРАТКО ТЕКСТ ОТЗЫВА',max_length = 1000,widget = forms.widgets.Textarea)
			
class Callorder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ',max_length = 20)

	phone_number=PhoneField(label = u'НОМЕР ТЕЛЕФОНА',code_length = 3, num_length = 7)

	question = forms.CharField(label=u'ВОПРОС',max_length = 1000, widget = forms.widgets.Textarea)
