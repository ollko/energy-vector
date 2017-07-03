# coding=utf-8
from django.shortcuts import render
from .models import Genset
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
	success_url = reverse_lazy('catalog:genset_list')

class GensetDelete(PermissionRequiredMixin, DeleteView):
	permission_required = 'genset.can_delete'
	model = Genset
	success_url = reverse_lazy('catalog:genset_list')	



