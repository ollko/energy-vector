# coding=utf-8
from django import forms
# from .widgets import MultiFileInput, PhoneField


# from django.core.exceptions import ValidationError

# def validate_images_format(file_instance):

# 	if file_instance.content_type=='image/jpeg':
# 		print 'file_instance.content_type=',file_instance.content_type
		
# 		raise ValidationError("Файл в 'jpeg' формате нельзя загрузить на сайт!")

			
class Callorder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА', max_length = 12, initial='+71234567890',)

	question = forms.CharField(label=u'ВОПРОС',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ЖЕЛАТЕЛЬНО УКАЗАТЬ', required = False )


class MaintenanceOrder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ:',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА:', max_length = 12, initial='+71234567890',)

	model = forms.CharField(label=u'МОДЕЛЬ ОБОРУДОВАНИЯ:',max_length = 100, initial = "УКАЖИТЕ МОДЕЛЬ ОБОРУДОВАНИЯ")

	place = forms.CharField(label=u'ВАШ РЕГИОН:', max_length = 100, initial = "ГДЕ НАХОДИТСЯ ОБОРУДОВАНИЕ",)

	questions = forms.CharField(label=u'ВАШИ ВОПРОСЫ ПО ТЕХ ОБСЛУЖИВАНИЮ:',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ВАШИ ВОПРОСЫ', required = False )

class RepairOrder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ:',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА:', max_length = 12, initial='+71234567890',)

	model = forms.CharField(label=u'МОДЕЛЬ ОБОРУДОВАНИЯ:',max_length = 100, initial = "УКАЖИТЕ МОДЕЛЬ ОБОРУДОВАНИЯ")

	place = forms.CharField(label=u'ВАШ РЕГИОН:', max_length = 100, initial = "ГДЕ НАХОДИТСЯ ОБОРУДОВАНИЕ",)

	questions = forms.CharField(label=u'ОПИШИТЕ ПРОБЛЕМУ:',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ХОРОШО БЫ ЗАПОЛНИТЬ', required = False )
