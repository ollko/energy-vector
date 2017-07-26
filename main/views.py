# coding=utf-8
from django.shortcuts import render
from .forms import Callorder, MaintenanceOrder, RepairOrder
from django.views.generic import TemplateView
from generic.mixins import GensetengineListMixin
from catalog.models import Gensetengine
from services.models import Service
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
class MainPageView(TemplateView, GensetengineListMixin):
	template_name = "end_templates/index.html"

def call_order(request):
	gensetengines = Gensetengine.objects.all()
	services = Service.objects.all()

	# путь для перенаправления при успешной отправке письма, или при отказе от заказа звонка:
	
	# next_path = request.META.get('HTTP_REFERER','/')
	    # if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = Callorder(request.POST)
		# check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
			# print 'form.cleaned_data= ',form.cleaned_data
			name = form.cleaned_data['name']
			phone_number = form.cleaned_data['phone_number']
			question = form.cleaned_data['question']
			if not question:
				question = u'У матросов нет вопросов.'
			if name and phone_number and question:
				text = u'Кому позвонить: '+unicode(name)+u"\nTелефон: "+phone_number+u'\nВопрос: '+question
				try:
					send_mail(u'Заявка на обратный звонок', text, 'energy-vector@energy-vector.ru',
						    ['korotkaya.olga@yandex.ru','lnv@energy-vector.ru'], fail_silently=False)
				except  BadHeaderError:
					return HttpResponse('Invalid header found.')
				
				# redirect to a new URL:

				return HttpResponseRedirect('/')		
	else:
		form = Callorder()

	return render(request,'main/call_order_form.html',
					{'form':form,'gensetengines':gensetengines,'services':services })


def maintenance_order_dgu(request):
	gensetengines = Gensetengine.objects.all()
	services = Service.objects.all()
	form_title =u'ЗАЯВКА НА ТЕХОБСЛУЖИВАНИЕ ДГУ'
	action_link ='/maintenance_order_dgu/'

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = MaintenanceOrder(request.POST)
		# check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
			# print 'form.cleaned_data= ',form.cleaned_data
			name = form.cleaned_data['name']
			phone_number = form.cleaned_data['phone_number']
			
			model = form.cleaned_data['model']

			place = form.cleaned_data['place']

			questions = form.cleaned_data['questions']

			if not questions:
				questions = u'Свяжитесь с нами и все узнаете.'
			if name and phone_number:
				text = u'Меня зовут: '+name+u"\nпрошу Вас перезвонить мне на номер: "+phone_number
				
				if model:
					text+=(u"модель ДГУ: "+model)
				if place:
					text+=(u'Местоположение ДГУ: '+place)
				text+=(u'Вопросы по техобслуживанию ДГУ:'+u'\n'+questions)
				title = u'Заявка на техобслуживание ДГУ'
				try:
					send_mail(title, text, 'energy-vector@energy-vector.ru',
						    ['korotkaya.olga@yandex.ru',], fail_silently=False)
				except  BadHeaderError:
					return HttpResponse('Invalid header found.')
				
				# redirect to a new URL:

				return HttpResponseRedirect('/')		
	else:
		form = MaintenanceOrder()
		
	return render(request,'main/service_order_form.html',
					{'form':form, 'form_title':form_title, 'action_link':action_link,
					'gensetengines':gensetengines,'services':services })

def maintenance_order_ups(request):
	gensetengines = Gensetengine.objects.all()
	services = Service.objects.all()
	form_title =u'ЗАЯВКА НА ТЕХОБСЛУЖИВАНИЕ ИБП'
	action_link ='/maintenance_order_ups/'

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = MaintenanceOrder(request.POST)
		# check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
			# print 'form.cleaned_data= ',form.cleaned_data
			name = form.cleaned_data['name']
			phone_number = form.cleaned_data['phone_number']
			
			model = form.cleaned_data['model']

			place = form.cleaned_data['place']

			questions = form.cleaned_data['questions']

			if not questions:
				questions = u'Свяжитесь с нами и все узнаете.'
			if name and phone_number:
				text = u'Меня зовут: '+name+u"\nпрошу Вас перезвонить мне на номер: "+phone_number
				
				if model:
					text+=(u"модель ИБП: "+model)
				if place:
					text+=(u'Местоположение ИБП: '+place)
				text+=(u'Вопросы по техобслуживанию ИБП:'+u'\n'+questions)
				title = u'Заявка на техобслуживание ИБП '
				try:
					send_mail(title, text, 'energy-vector@energy-vector.ru',
						    ['korotkaya.olga@yandex.ru',], fail_silently=False)
				except  BadHeaderError:
					return HttpResponse('Invalid header found.')
				
				# redirect to a new URL:

				return HttpResponseRedirect('/')		
	else:
		form = MaintenanceOrder()

	return render(request,'main/service_order_form.html',
					{'form':form, 'form_title':form_title, 'action_link':action_link,
					'gensetengines':gensetengines,'services':services })


def repair_order_dgu(request):
	gensetengines = Gensetengine.objects.all()
	services = Service.objects.all()
	action_link ='/repair_order_dgu/'
	form_title ='ЗАЯВКА НА РЕМОНТ ДГУ'

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = RepairOrder(request.POST)
		# check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
			# print 'form.cleaned_data= ',form.cleaned_data
			name = form.cleaned_data['name']
			phone_number = form.cleaned_data['phone_number']
			
			model = form.cleaned_data['model']

			place = form.cleaned_data['place']

			questions = form.cleaned_data['questions']

			if not questions:
				questions = u'Свяжитесь с нами и все узнаете.'
			if name and phone_number:
				text = u'Меня зовут: '+name+u"\nпрошу Вас перезвонить мне на номер: "+phone_number
				if model:
					text+=(u"\nМодель оборудования: "+model)
				if place:
					text+=(u'\nМестоположение оборудования: '+place)
				if questions:
					text+=(u'\nЧто случилось с ДГУ: '+u'\n'+questions)
				title=u'Заявка на ремонт ДГУ'
				try:
					send_mail(title, text, 'energy-vector@energy-vector.ru',
						    ['korotkaya.olga@yandex.ru',], fail_silently=False)
				except  BadHeaderError:
					return HttpResponse('Invalid header found.')
				
				# redirect to a new URL:

				return HttpResponseRedirect('/')		
	else:
		form = RepairOrder()
		
		
	return render(request,'main/service_order_form.html',
					{'form':form, 'form_title':form_title, 'action_link':action_link,
					'gensetengines':gensetengines,'services':services })


def repair_order_ups(request):
	gensetengines = Gensetengine.objects.all()
	services = Service.objects.all()
	form_title =u'ЗАЯВКА НА РЕМОНТ ИБП'
	action_link ='/repair_order_ups/'

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = RepairOrder(request.POST)
		# check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
			# print 'form.cleaned_data= ',form.cleaned_data
			name = form.cleaned_data['name']
			phone_number = form.cleaned_data['phone_number']
			
			model = form.cleaned_data['model']

			place = form.cleaned_data['place']

			questions = form.cleaned_data['questions']

			if not questions:
				questions = u'Свяжитесь с нами и все узнаете.'
			if name and phone_number:
				text = u'Меня зовут: '+name+u"\nпрошу Вас перезвонить мне на номер: "+phone_number
				if model:
					text+=(u"\nМодель оборудования: "+model)
				if place:
					text+=(u'\nМестоположение оборудования: '+place)
				if questions:
					text+=(u'\nЧто случилось с ИБП: '+u'\n'+questions)
				title=u'Заявка на ремонт ИБП'
				try:
					send_mail(title, text, 'energy-vector@energy-vector.ru',
						    ['korotkaya.olga@yandex.ru',], fail_silently=False)
				except  BadHeaderError:
					return HttpResponse('Invalid header found.')
				
				# redirect to a new URL:

				return HttpResponseRedirect('/')		
	else:
		form = RepairOrder()
		
	return render(request,'main/service_order_form.html',
					{'form':form, 'form_title':form_title, 'action_link':action_link,
					'gensetengines':gensetengines,'services':services })
