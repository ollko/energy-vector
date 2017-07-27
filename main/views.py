# coding=utf-8
from django.shortcuts import render, HttpResponseRedirect
from .forms import Callorder, ServiceOrder
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from generic.mixins import GensetengineListMixin
from catalog.models import Gensetengine
from services.models import Service
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
class MainPageView(TemplateView, GensetengineListMixin):
	template_name = "main/index.html"

class CallorderFormView(SuccessMessageMixin, FormView, GensetengineListMixin):
	
	template_name = 'main/call_order_form.html'
	form_class = Callorder
	success_url = '/'
	success_message = 'Ваша заявка на обратный звонок успешно отправлена !!!' 
	

	def form_valid(self, form):
		form.send_email()
		# This method is called when valid form_class data has been POSTed.
        # It should return an HttpResponse.
        
		return super(CallorderFormView, self).form_valid(form)

class ServiceOrderFormView(SuccessMessageMixin, FormView,  GensetengineListMixin):
	
	template_name = 'main/service_order_form.html'
	form_class = ServiceOrder
	success_url = '/'
	success_message = 'Ваша заявка на успешно отправлена !!!' 
	
	SERVICE_TYPES = {
		'maintenance':'ТЕХОБСЛУЖИВАНИЕ',
		'repair':'РЕМОНТ',
		'dgu':'ДГУ',
		'ups':'ИБП'
	}
	serv_type = None
	equip_type = None
	def get(self, request, *args, **kwargs):
	    self.serv_type = self.kwargs['serv_type']
	    self.equip_type = self.kwargs['equip_type']
	    return super(ServiceOrderFormView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(ServiceOrderFormView, self).get_context_data(**kwargs)
		print 'context =', context

		context['serv_type_ru'] = self.SERVICE_TYPES[self.serv_type]
		context['equip_type_ru'] = self.SERVICE_TYPES[self.equip_type]
		context['serv_type'] = self.serv_type
		context['equip_type'] = self.equip_type

		return context

	def post(self, request, *args, **kwargs):
	    """
	    Handles POST requests, instantiating a form instance with the passed
	    POST variables and then checked for validity.
	    """
	    form_class = self.get_form_class()
	    form = self.get_form(form_class)
	    if form.is_valid():
	    	x=self.SERVICE_TYPES[self.kwargs['equip_type']].decode('utf-8')
	    	y = self.SERVICE_TYPES[self.kwargs['serv_type']].decode('utf-8')
	    	print 'type(x)=',type(x)
	    	print 'type(y)=',type(y)

	    	form.send_email(x,y)
	        return self.form_valid(form)
	    else:
	        return self.form_invalid(form)

