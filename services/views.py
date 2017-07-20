# coding=utf-8
from django.shortcuts import render

from catalog.models import Gensetengine
from .models import Service
from django.core.mail import send_mail, BadHeaderError

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from generic.mixins import GensetengineListMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class ServiceDetailView(DetailView, GensetengineListMixin):
	model = Service


class ServiceCreate(PermissionRequiredMixin, CreateView, GensetengineListMixin):
	permission_required = 'service.can_add'
	model = Service
	fields = '__all__'
	context_object_name = 'services'	
	

class ServiceUpdate(PermissionRequiredMixin, UpdateView, GensetengineListMixin):
	permission_required = 'service.can_change'
	model = Service
	fields = '__all__'
	

class ServiceDelete(PermissionRequiredMixin, DeleteView, GensetengineListMixin):
	permission_required = 'service.can_delete'
	model = Service
	success_url = reverse_lazy('company:main_page')
	def get_context_data(self, **kwargs):
		context = super(ServiceDelete, self).get_context_data(**kwargs)
		context['back_url'] = '/services/'+ self.kwargs['pk']
		print "context['back_url']=",context
		return context


def send_request(request):
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

	return render(request,'services/call_order_form.html',
					{'form':form,'gensetengines':gensetengines })