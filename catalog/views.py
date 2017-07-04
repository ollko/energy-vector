# coding=utf-8
from django.shortcuts import render
from .models import Genset, Gensetengine
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class GensetList(ListView):
	model = Genset
	template_name = 'catalog/gensetlist.html'
	context_object_name = 'gensets'

class GensetListCorr(PermissionRequiredMixin, ListView):
	permission_required = ('genset.can_change', 'genset.can_delete')
	model = Genset
	template_name = 'catalog/gensetlistcorr.html'
	context_object_name = 'gensets'		

class GensetCreate(PermissionRequiredMixin, CreateView):
	permission_required = 'genset.can_add'
	model = Genset
	fields = '__all__'
	success_url = reverse_lazy('catalog:genset_list')
	
class GensetUpdate(PermissionRequiredMixin, UpdateView):
	permission_required = 'genset.can_change'
	model = Genset
	fields = '__all__'
	success_url = reverse_lazy('catalog:genset_list_corr')

class GensetDelete(PermissionRequiredMixin, DeleteView):
	permission_required = 'genset.can_delete'
	model = Genset
	success_url = reverse_lazy('catalog:genset_list_corr')	

class GensetengineListCorr(PermissionRequiredMixin, ListView):
	permission_required = ('gensetengine.can_change', 'gensetengine.can_delete')
	model = Gensetengine
	template_name = 'catalog/gensetengine_listcorr.html'
	context_object_name = 'gensetengines'	

class GensetengineCreate(PermissionRequiredMixin, CreateView):
	permission_required = 'gensetengine.can_add'
	model = Gensetengine
	fields = '__all__'
	success_url = reverse_lazy('catalog:genset_list')
	
class GensetengineUpdate(PermissionRequiredMixin, UpdateView):
	permission_required = 'gensetengine.can_change'
	model = Gensetengine
	fields = '__all__'
	success_url = reverse_lazy('catalog:genset_list_corr')

class GensetengineDelete(PermissionRequiredMixin, DeleteView):
	permission_required = 'gensetengine.can_delete'
	model = Gensetengine
	success_url = reverse_lazy('catalog:genset_list_corr')	

