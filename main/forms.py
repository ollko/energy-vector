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

class MaintenanceOrder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ:',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА:', max_length = 12, initial='+71234567890',)

	model = forms.CharField(label=u'МОДЕЛЬ ОБОРУДОВАНИЯ:',max_length = 100, initial = "УКАЖИТЕ ЕСЛИ ВОЗМОЖНО")

	place = forms.CharField(label=u'ВАШ РЕГИОН:', max_length = 100, initial = "ГДЕ НАХОДИТСЯ ОБОРУДОВАНИЕ",)

	questions = forms.CharField(label=u'ВАШИ ВОПРОСЫ ПО ТЕХ ОБСЛУЖИВАНИЮ:',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ВАШИ ВОПРОСЫ', required = False )

class RepairOrder(forms.Form):

	name = forms.CharField(label=u'ВАШЕ ИМЯ:',max_length = 20, initial = "ВАШЕ ИМЯ",)

	phone_number=forms.CharField(label = u'НОМЕР ТЕЛЕФОНА:', max_length = 12, initial='+71234567890',)

	model = forms.CharField(label=u'МОДЕЛЬ ОБОРУДОВАНИЯ:',max_length = 100, initial = "УКАЖИТЕ ЕСЛИ ВОЗМОЖНО")

	place = forms.CharField(label=u'ВАШ РЕГИОН:', max_length = 100, initial = "ГДЕ НАХОДИТСЯ ОБОРУДОВАНИЕ",)

	questions = forms.CharField(label=u'ОПИШИТЕ ПРОБЛЕМУ:',max_length = 1000, 
		widget = forms.widgets.Textarea, initial = 'ХОРОШО БЫ ЗАПОЛНИТЬ', required = False )
