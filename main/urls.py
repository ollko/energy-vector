# coding=utf-8
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main'
urlpatterns = [

	url(r'^$', views.MainPageView.as_view(), name='main_page',),

	url(r'^call_order/$', views.call_order,   name='call_order',),
	
	url(r'^maintenance_order_dgu/$', views.maintenance_order_dgu,   name='maintenance_order_dgu',),

	url(r'^maintenance_order_ups/$', views.maintenance_order_ups,   name='maintenance_order_ups',),

	url(r'^repair_order_dgu/$', views.repair_order_dgu,   name='repair_order_dgu',),

	url(r'^repair_order_ups/$', views.repair_order_ups,   name='repair_order_ups',),

	url(r'^login/', auth_views.login,
		{"template_name":"end_templates/login.html"}, name='login'),
	url(r'^logout/', auth_views.logout, name='logout'),

]