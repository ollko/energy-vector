# coding=utf-8
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main'
urlpatterns = [

	url(r'^$', views.MainPageView.as_view(), name='main_page',),

	url(r'^call_order/$', views.CallorderFormView.as_view(),   name='call_order',),

	url(r'^order/(?P<serv_type>maintenance|repair)/(?P<equip_type>dgu|ups)/$',
						views.ServiceOrderFormView.as_view(),   name='service_order1',),

	url(r'^login/', auth_views.login,
		{"template_name":"end_templates/login.html"}, name='login'),
	url(r'^logout/', auth_views.logout, name='logout'),

]