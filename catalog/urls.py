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

    url(r'^dgu/perkins/(?P<pk>\d+)/update/$', views.GensetDelete.as_view(), 
						    	name='genset_update',),

	url(r'^dgu/perkins/(?P<pk>\d+)/delete/$', views.GensetDelete.as_view(), 
								name='genset_delete',),

]