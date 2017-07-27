# coding=utf-8
from django import forms
from django.core.mail import send_mail, BadHeaderError

			
class Callorder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА', max_length = 12, initial='+71234567890',)

	question = forms.CharField(label=u'ВОПРОС',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ЖЕЛАТЕЛЬНО УКАЗАТЬ', required = False )

	def send_email(self):

		name = self.cleaned_data['name']
		phone_number = self.cleaned_data['phone_number']
		question = self.cleaned_data['question']
		if not question:
			question = u'У матросов нет вопросов.'
		if name and phone_number:
			text = u'Кому позвонить: '+unicode(name)+u"\nTелефон: "+phone_number+u'\nВопрос: '+question
			mail_title = u'Заявка на обратный звонок'
			try:
				send_mail(mail_title, text, 'energy-vector@energy-vector.ru',
					    ['korotkaya.olga@yandex.ru',], fail_silently=False)
			except  BadHeaderError:
				return HttpResponse('Invalid header found.')
		pass

class ServiceOrder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ:',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА:', max_length = 12, initial='+71234567890',)

	model = forms.CharField(label=u'МОДЕЛЬ ОБОРУДОВАНИЯ:',max_length = 100, initial = "УКАЖИТЕ ЕСЛИ ВОЗМОЖНО")

	place = forms.CharField(label=u'ВАШ РЕГИОН:', max_length = 100, initial = "ГДЕ НАХОДИТСЯ ОБОРУДОВАНИЕ",)

	questions = forms.CharField(label=u'ВАШИ ВОПРОСЫ:',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ВАШИ ВОПРОСЫ', required = False )	

	def send_email(self, equipment_type, service_type):
		name = self.cleaned_data['name']
		phone_number = self.cleaned_data['phone_number']
		
		model = self.cleaned_data['model']

		place = self.cleaned_data['place']

		questions = self.cleaned_data['questions']

		if not questions:
			questions = u'Свяжитесь с нами и все узнаете.'
		if name and phone_number:
			text = u'Меня зовут: '+name+u"\nПерезвоните мне на номер: "+phone_number
			
			if model:
				text+=(u"\nМодель "+": "+model)
			if place:
				text+=(u'\nМестоположение '+equipment_type+": "+place)
			text+=u'\nВопросы по '+service_type+u' '+equipment_type+u": "+questions
			title = u'Заявка на '+service_type+u' '+equipment_type
			try:
				send_mail(title, text, 'energy-vector@energy-vector.ru',
					    ['korotkaya.olga@yandex.ru',], fail_silently=False)
			except  BadHeaderError:
				return HttpResponse('Invalid header found.')
		pass
# class MaintenanceOrder(forms.Form):

# 	name = forms.CharField(label=u'ВАШЕ ИМЯ:',max_length = 20, initial = "ВАШЕ ИМЯ",)

# 	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА:', max_length = 12, initial='+71234567890',)

# 	model = forms.CharField(label=u'МОДЕЛЬ ОБОРУДОВАНИЯ:',max_length = 100, initial = "УКАЖИТЕ ЕСЛИ ВОЗМОЖНО")

# 	place = forms.CharField(label=u'ВАШ РЕГИОН:', max_length = 100, initial = "ГДЕ НАХОДИТСЯ ОБОРУДОВАНИЕ",)

# 	questions = forms.CharField(label=u'ВАШИ ВОПРОСЫ ПО ТЕХ ОБСЛУЖИВАНИЮ:',max_length = 1000, 
# 		widget = forms.widgets.Textarea, initial = 'ВАШИ ВОПРОСЫ', required = False )

# class RepairOrder(forms.Form):

# 	name = forms.CharField(label=u'ВАШЕ ИМЯ:',max_length = 20, initial = "ВАШЕ ИМЯ",)

# 	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА:', max_length = 12, initial='+71234567890',)

# 	model = forms.CharField(label=u'МОДЕЛЬ ОБОРУДОВАНИЯ:',max_length = 100, initial = "УКАЖИТЕ ЕСЛИ ВОЗМОЖНО")

# 	place = forms.CharField(label=u'ВАШ РЕГИОН:', max_length = 100, initial = "ГДЕ НАХОДИТСЯ ОБОРУДОВАНИЕ",)

# 	questions = forms.CharField(label=u'ОПИШИТЕ ПРОБЛЕМУ:',max_length = 1000, 
# 		widget = forms.widgets.Textarea, initial = 'ХОРОШО БЫ ЗАПОЛНИТЬ', required = False )
