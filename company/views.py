# coding=utf-8
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'company/index.html',)

