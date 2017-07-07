# coding=utf-8
from django.conf.urls import url
from . import views as my_views
from django.contrib.flatpages import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'company'
urlpatterns = [

    url(r'^$', my_views.index,   name='index',),

    url(r'^send-email/$', my_views.send_email,   name='send_email',),

    url(r'^sro/$', my_views.SroView.as_view(),),

    url(r'^certificates/$', my_views.CertificateList.as_view(), name='certificates'),

    url(r'^certificates_new/$', my_views.certificates_new, name='certificates_new'),
    url(r'^certificate_list_del/$', my_views.certificate_list_del, name='certificate_list_del'),


    url(r'^otzivi/$', my_views.OtzivList.as_view(), name='otzivi'),
    url(r'^otzivi_new/$', my_views.otziv_new, name='otziv_new'),
    url(r'^otziv_corr/$', my_views.OtzivCorr.as_view(), name='otziv_corr'),
    url(r'^otziv_corr/(?P<otziv_id>\d+)/$', my_views.otziv_corr_detail, name='otziv_corr_detail'),
    url(r'^otziv_del/$', my_views.otziv_list_del, name='otziv_del'),

    url(r'^documents/$', TemplateView.as_view(template_name="end_templates/in_the_development.html"),),

    url(r'^contacts/$', views.flatpage, {'url':'/contacts/'}, name='contacts'),

    url(r'^login/', auth_views.login,
        {"template_name":"end_templates/login.html"}, name='login'),

    url(r'^logout/', auth_views.logout, 
        name='logout'),

]