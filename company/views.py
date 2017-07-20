# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from .models import Marka, Certificate, Otziv, Callorderuser
from catalog.models import Gensetengine
from .forms import CertificateForm, OtzivForm, Callorder
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError

from django.views.generic import TemplateView
from generic.mixins import GensetengineListMixin

import re


# Create your views here.
class DocumentsView(TemplateView, GensetengineListMixin):
	template_name="end_templates/in_the_development.html"

class SroView(TemplateView, GensetengineListMixin):
	template_name="company/sro.html"

class ContactsView(TemplateView, GensetengineListMixin):
	template_name="company/contacts.html"
				
class MainPageView(TemplateView, GensetengineListMixin):
	template_name = "end_templates/index.html"
	

def send_email(request):
	gensetengines = Gensetengine.objects.all()
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

	return render(request,'callorder/call_order_form.html',
					{'form':form,'gensetengines':gensetengines })

class CertificateList(ListView, GensetengineListMixin):
	model = Certificate
	

class OtzivList(ListView, GensetengineListMixin):
	'''Выводится страница с отзывами о компании
	'''
	model = Otziv
	template_name = 'company/otziv_list.html'
	context_object_name = 'otzivs'


class OtzivCorr(ListView, GensetengineListMixin):
	'''
	выводится страница, где можно выбрать отзыв для корректировки
	'''
	model = Otziv
	template_name = 'company/otziv_list_corr.html'
	context_object_name = 'otzivs'


@permission_required('company.delete_otziv')
@login_required
def otziv_list_del(request):
	gensetengines = Gensetengine.objects.all()

	otzivs = Otziv.objects.all()
	do_choice=0
	
	if request.method =='POST':
		error=None
		for otziv in otzivs:
			if unicode(otziv.id) in request.POST:
				otziv.delete()
				do_choice=1
		if do_choice==1:
			return HttpResponseRedirect('/otzivi/')
		else:
			error=u'**Вы не выбрали не одного отзыва для удаления!'				
			return render(request, 'company/otziv_list_del.html',
					{'otzivs':otzivs, 'error':error, 'gensetengines':gensetengines})
	else:
		return render(request, 'company/otziv_list_del.html',
			{'otzivs':otzivs, 'gensetengines':gensetengines})


@permission_required('company.delete_certificate')
@login_required
def certificate_list_del(request):
	gensetengines = Gensetengine.objects.all()

	certificates = Certificate.objects.all()
	do_choice = 0

	if request.method =='POST':
		error=None
		for certificate in certificates:
			if unicode(certificate.id) in request.POST:				
				certificate.delete()
				do_choice=1
		if do_choice==1:
			return HttpResponseRedirect('/certificates/')
		else:
			error=u'**Вы не выбрали не одного сертификата для удаления!'				
			return render(request, 'company/certificate_list_del.html',
							{'certificates':certificates, 'error':error})
	else:
		return render(request, 'company/certificate_list_del.html',
			{'certificates':certificates, 'gensetengines':gensetengines})






@permission_required('company.add_certificate')
@login_required		
def certificates_new(request):
	gensetengines = Gensetengine.objects.all()

	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = CertificateForm(request.POST, request.FILES)
		
		if form.is_valid():
		
			certificates = request.FILES
			
			i=len(certificates.getlist('certificate'))-1
			
			while i>=0:

				certificate = certificates.getlist('certificate')[i]
				
				c = Certificate( certificate = certificate)

				c.save()

				c.certificate_1x_2x()
				
				c.save()
				i=i-1			

			return HttpResponseRedirect('/certificates/')
    # if a GET (or any other method) we'll create a blank form
	else:
		form = CertificateForm()


	return render(request,  'company/certificates_new_form.html', {'form': form,
					    	'title':'выберите файлы с сертификатами',
					    	'value':'добавить',
					    	'enctype_atr':'multipart/form-data',
					    	'gensetengines':gensetengines
					    	})




@permission_required('company.add_otziv')
@login_required		
def otziv_new(request):
	gensetengines = Gensetengine.objects.all()

	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = OtzivForm(request.POST,request.FILES)
		
		if form.is_valid():
			# process the data in form.cleaned_data as required
			
			t = form.cleaned_data['text']
			# t_list=re.split(r'\n+',t)
			# text='*|*'.join(t_list)

			otziv = request.FILES['otziv']
			print 'otziv=',otziv	
			o = Otziv(text = t, otziv = otziv)

			o.save()

			o.otziv_1x_2x()
			
			o.save()		

			return HttpResponseRedirect('/otzivi/')
    # if a GET (or any other method) we'll create a blank form
	else:
		form = OtzivForm()


	return render(request,  'company/otziv_new_form.html', {'form': form,
					    		'enctype_atr':'multipart/form-data',
					    		'gensetengines':gensetengines
					    	})


@permission_required('company.add_otziv')
@login_required		
def otziv_corr_detail(request,otziv_id):
	'''
	корректировка одного отзыва
	'''
	gensetengines = Gensetengine.objects.all()

	otziv=get_object_or_404(Otziv,pk=otziv_id)
	
	if request.method =='POST':

		form=OtzivForm(request.POST,request.FILES, instance=otziv)

		if form.is_valid():
			form.cleaned_data
			form.save()
			
			o=get_object_or_404(Otziv,pk=otziv_id)
			o.otziv_1x_2x()	
			o.save()

		return HttpResponseRedirect('/otzivi/')	

	else:
		form = OtzivForm(instance=otziv)

	return render(request, 'company/otziv_corr_detail.html',
						{'form':form,'gensetengines':gensetengines})	
