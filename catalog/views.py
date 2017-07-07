# coding=utf-8
from django.shortcuts import render
from .models import Genset, Gensetengine
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ProcessFormView
from django.views.generic.base import ContextMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class GensetengineListMixin(ContextMixin):
	def get_context_data(self, **kwargs):
		context = super(GensetengineListMixin, self).get_context_data(**kwargs)
		context["gensetengines"] = Gensetengine.objects.all()
		return context

class GensetList(ListView, GensetengineListMixin):
	model = Genset
	template_name = 'catalog/gensetlist.html'
	context_object_name = 'gensets'
	def get_queryset(self):
		return Genset.objects.filter(gensetengine__id = self.kwargs['gensetengine_id'])
	def get_context_data(self, **kwargs):
		context = super(GensetList, self).get_context_data(**kwargs)
		context['gensetengine'] = Gensetengine.objects.get(pk=self.kwargs['gensetengine_id'])
		return context

class GensetListCorr(PermissionRequiredMixin, ListView, GensetengineListMixin):
	permission_required = ('genset.can_change', 'genset.can_delete')
	model = Genset
	template_name = 'catalog/gensetlistcorr.html'
	context_object_name = 'gensets'
	def get_queryset(self):
		return Genset.objects.filter(gensetengine__id = self.kwargs['gensetengine_id'])	
	def get_context_data(self, **kwargs):
		context = super(GensetListCorr, self).get_context_data(**kwargs)
		context['gensetengine'] = Gensetengine.objects.get(pk=self.kwargs['gensetengine_id'])
		return context

class GensetCreate(PermissionRequiredMixin, CreateView, GensetengineListMixin):
	permission_required = 'genset.can_add'
	model = Genset
	fields = '__all__'

	def post(self, request, *args, **kwargs):
		self.success_url = reverse_lazy('catalog:genset_list', kwargs= {'gensetengine_id':self.kwargs['gensetengine_id']})
		return super(GensetCreate, self).post(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(GensetCreate, self).get_context_data(**kwargs)
		context['gensetengine_pk'] = Gensetengine.objects.get(pk=self.kwargs['gensetengine_id']).pk
		return context



class GensetUpdate(PermissionRequiredMixin, UpdateView, GensetengineListMixin):
	permission_required = 'genset.can_change'
	model = Genset
	fields = '__all__'
	def post(self, request, *args, **kwargs):
		self.success_url = reverse_lazy('catalog:genset_list_corr',
			kwargs= {'gensetengine_id':Genset.objects.get(pk=self.kwargs['pk']).gensetengine.pk})
		return super(GensetUpdate, self).post(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(GensetUpdate, self).get_context_data(**kwargs)
		context['gensetengine_pk'] = Genset.objects.get(pk=self.kwargs['pk']).gensetengine.pk
		return context

class GensetDelete(PermissionRequiredMixin, DeleteView, GensetengineListMixin):
	permission_required = 'genset.can_delete'
	model = Genset
	def post(self, request, *args, **kwargs):
		self.success_url = reverse_lazy('catalog:genset_list_corr',
			kwargs= {'gensetengine_id':Genset.objects.get(pk=self.kwargs['pk']).gensetengine.pk})
		return super(GensetDelete, self).post(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(GensetDelete, self).get_context_data(**kwargs)
		context['gensetengine_pk'] = Genset.objects.get(pk=self.kwargs['pk']).gensetengine.pk
		return context

class GensetengineCreate(PermissionRequiredMixin, CreateView, GensetengineListMixin):
	permission_required = 'gensetengine.can_add'
	model = Gensetengine
	fields = '__all__'
	
	def post(self, request, *args, **kwargs):
		self.success_url = reverse_lazy('catalog:genset_list',
						kwargs= {'gensetengine_id': unicode(int(Gensetengine.objects.last().id)+1)})
		return super(GensetengineCreate, self).post(request, *args, **kwargs)

class GensetengineListCorr(PermissionRequiredMixin, ListView, GensetengineListMixin):
	permission_required = ('gensetengine.can_change', 'gensetengine.can_delete')
	model = Gensetengine
	template_name = 'catalog/gensetengine_listcorr.html'
	context_object_name = 'gensetengines'	
	def get_context_data(self, **kwargs):
		context = super(GensetengineListCorr, self).get_context_data(**kwargs)
		context['gensetengine_id'] = Gensetengine.objects.first().pk
		return context

	
class GensetengineUpdate(PermissionRequiredMixin, UpdateView, GensetengineListMixin):
	permission_required = 'gensetengine.can_change'
	model = Gensetengine
	fields = '__all__'
	success_url = reverse_lazy('catalog:gensetengine_list_corr')

class GensetengineDelete(PermissionRequiredMixin, DeleteView, GensetengineListMixin):
	permission_required = 'gensetengine.can_delete'
	model = Gensetengine
	success_url = reverse_lazy('catalog:gensetengine_list_corr')	
