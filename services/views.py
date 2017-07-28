# coding=utf-8
from django.shortcuts import render

from catalog.models import Gensetengine
from .models import Service


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
	success_url = reverse_lazy('main:main_page')
	def get_context_data(self, **kwargs):
		context = super(ServiceDelete, self).get_context_data(**kwargs)
		context['back_url'] = '/services/'+ self.kwargs['pk']
		print "context['back_url']=",context
		return context


