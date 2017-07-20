# coding=utf-8
from django.conf.urls import url
from . import views 


app_name = 'services'
urlpatterns = [
	
	# url(r'^send_request/$', views.send_request,   name='send_request')

	url(r'^(?P<pk>\d+)/$', views.ServiceDetailView.as_view(), 
						    	name='service_detail',),

	url(r'^create/$', views.ServiceCreate.as_view(), 
						    	name='service_create',),

	url(r'^(?P<pk>\d+)/update/$', views.ServiceUpdate.as_view(), 
						    	name='service_update',),

	url(r'^(?P<pk>\d+)/delete/$', views.ServiceDelete.as_view(), 
								name='service_delete',),
]