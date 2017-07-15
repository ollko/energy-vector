# coding=utf-8
from django import forms

from .widgets import MultiFileInput, PhoneField
from .models import Callorderuser, Marka, Certificate, Otziv
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

class OtzivForm(forms.ModelForm):

	class Meta:
		model = Otziv
		fields = ['otziv','text']
		widgets = {
			'text':forms.widgets.Textarea()	
		}
			
		error_messages = {
            'name': {
                'max_length': "This writer's name is too long.",
            },
        }
			
class Callorder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА', max_length = 12, initial='+71234567890',)

	question = forms.CharField(label=u'ВОПРОС',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ЖЕЛАТЕЛЬНО УКАЗАТЬ', required = False )
