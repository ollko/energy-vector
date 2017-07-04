# coding=utf-8
from django.conf.urls import url
from . import views


app_name = 'catalog'
urlpatterns = [

    url(r'^dgu/perkins/$', views.GensetList.as_view(), 
						    	name='genset_list',),

    url(r'^dgu/perkins/corr/$', views.GensetListCorr.as_view(), 
						    	name='genset_list_corr',),

	url(r'^dgu/perkins/create/$', views.GensetCreate.as_view(), 
						    	name='genset_create',),

	url(r'^dgu/perkins/(?P<pk>\d+)/update/$', views.GensetUpdate.as_view(), 
						    	name='genset_update',),

	url(r'^dgu/perkins/(?P<pk>\d+)/delete/$', views.GensetDelete.as_view(), 
								name='genset_delete',),

	url(r'^dgu/gensetengine/corr/$', views.GensetengineListCorr.as_view(), 
						    	name='gensetengine_list_corr',),

	url(r'^dgu/gensetengine/create/$', views.GensetengineCreate.as_view(), 
						    	name='gensetengine_create',),

	url(r'^dgu/gensetengine/(?P<pk>\d+)/update/$', views.GensetengineUpdate.as_view(), 
						    	name='gensetengine_update',),

	url(r'^dgu/gensetengine/(?P<pk>\d+)/delete/$', views.GensetengineDelete.as_view(), 
								name='gensetengine_delete',),



]